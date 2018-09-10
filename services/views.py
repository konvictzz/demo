import markdown
import logging
from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from services import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from elasticsearch import Elasticsearch

# Create your views here.

# logging
logger = logging.getLogger(__name__)

'''
@login_required
def url(request):
	context_url = {}
	context_url['section'] = 'url' 
	# 因为 models 文件定义了 Meta ，所以无需指定 order_by
	#context_url["app_url"] = models.Server_URLs.objects.all().order_by('servertype')
	context_url["url_list"] = models.Server_URLs.objects.all()
	return render(request, 'services/url.html', context_url)
'''

class PaginationData:
	def pagination_data(self, paginator, page, is_paginated):
		# 如果没有分页，则无需显示分页
		# 不用任何分页导航条的数据，因此返回一个空的字典
		if is_paginated == False:
			return {}

		# 当前页左边连续的页码号，初始值为空
		left = []

		# 当前页右边连续的页码号，初始值为空
		right = []

		# 标示第 1 页页码后是否需要显示省略号
		left_has_more = False

		# 标示z最后一页页码前是否需要显示省略号
		right_has_more = False

		# 标示是否需要显示第 1 页或最后一页的页码号
		# 如果当前页左边的连续页码号中含有第 1 页或最后一页的页码号，则无需再显示
		# 默认初始值为False
		first = False
		last = False

		# 标识是否需要上一页和下一页
		# 默认为True
		has_previous_page = True
		has_next_page = True

		# 获得用户当前请求的页码号
		current_number = page.number

		# 获得分页后的总页数
		total_number = paginator.num_pages

		# 获得整个分页的页码列表，比如分了两页，则为range(1,3)
		page_range = paginator.page_range

		if current_number == 1:
			# 判断是否有前一页
			has_previous_page = page.has_previous

			# 如果当前页为第一页，则当前页的左边不需要数据
			# 此时只要获得当前页右边的连续页码号
			# 这里将获得当前页码后连续两个页码
			right = page_range[current_number:current_number + 2]

			# 如果最右边的页码号比总页数减去1还要小
			# 说明最右边的页码号和最后一页的页码号之间还有其他页码，因此需要显示省略号
			if right[-1] < total_number - 1:
				right_has_more = True

			# 如果最右边的页码号比总页数要小
			# 说明当前页右边的连续页码号中不包含最后一页，所以需要显示最后一页的页码号
			if right[-1] < total_number:
				last = True

		elif current_number == total_number:
			# 判断是否有下一页
			has_next_page = page.has_next
			# 如果请求最后一页，则当前页左边右边不再需要数据
			# 此时需要获得当前页左边的连续页码号
			left =  page_range[(current_number - 3) if (current_number - 3) > 0 else 0:current_number -1]

			# 如果最左边的页码号比2还大，说明和第 1 页之间有其他页码，需要显示省略号
			if left[0] > 2:
				left_has_more = True
			# 如果最左边的页码号比1大，说明不包含第 1 页，需要显示第 1 页的页码号
			if left[0] > 1:
				first = True

		else:
			# 如果请求的既不是第 1 页也不是最后一页，则需要获得左右两边的连续页码号
			# 同样还是获取当前页码前后的连续两个页面
			left =  page_range[(current_number - 3) if (current_number - 3) > 0 else 0:current_number -1]
			right = page_range[current_number:current_number + 2]

			# 是否需要显示最后一页和最后一页前的省略号
			if right[-1] < total_number - 1:
				right_has_more = True
			if right[-1] < total_number:
				last = True

			# 是否需要显示第 1 页和第 1 页后的省略号				
			if left[0] > 2:
				left_has_more = True
			if left[0] > 1:
				first = True

		data = {
			'left': left,
			'right': right,
			'left_has_more': left_has_more,
			'right_has_more': right_has_more,
			'first': first,
			'last': last,
			'has_next_page': has_next_page,
			'has_previous_page': has_previous_page,
		}

		return data


class UrlView(LoginRequiredMixin, ListView, PaginationData):

	model = models.Server_URLs
	template_name = "services/url.html"
	context_object_name = "url_list"
	paginate_by = 15

	def get_context_data(self, **kwargs):
		logger.info("进入UrlView查询")
		context_url = super(UrlView, self).get_context_data(**kwargs)
		context_url['section'] = 'url'
		context_url['error_msg'] = ''

		# 生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量
		# 由于 context_url 是一个字典，所以调用 get 方法从中取出某个键对应的值
		paginator = context_url.get('paginator')
		page = context_url.get('page_obj')
		is_paginated = context_url.get('is_paginated')

		pagination_data = self.pagination_data(paginator, page, is_paginated)
		context_url.update(pagination_data)
		logger.info("查询UrlView完成")
		return context_url

'''
# 以下方法已经不再使用，修改为通用视图方法
def environment_type(request, pk):
	context_environment = {}
	context_environment['section'] = 'url'
	type = get_object_or_404(models.Server_Type, pk=pk)
	context_environment["url_list"] = models.Server_URLs.objects.filter(servertype=type)
	return render(request, 'services/url.html', context_environment)
'''

class Environment_typeView(LoginRequiredMixin, ListView, PaginationData):

	model = models.Server_URLs
	template_name = "services/url.html"
	context_object_name = "url_list"
	paginate_by = 15

	def get_queryset(self):
		type = get_object_or_404(models.Server_Type, pk=self.kwargs.get('pk'))
		return super(Environment_typeView, self).get_queryset().filter(servertype=type)

	def get_context_data(self, **kwargs):
		context_environment = super(Environment_typeView, self).get_context_data(**kwargs)
		context_environment['section'] = 'url'
		context_environment['error_msg'] = ''

		paginator = context_environment.get('paginator')
		page = context_environment.get('page_obj')
		is_paginated = context_environment.get('is_paginated')

		pagination_data = self.pagination_data(paginator, page, is_paginated)
		context_environment.update(pagination_data)		
		return context_environment

@login_required
def url_detail(request, pk):
	context_url_detail = {}
	context_url_detail['section'] = 'url'
	context_url_detail['url'] = get_object_or_404(models.Server_URLs, pk=pk)
	context_url_detail['url'].required_database =  markdown.markdown(context_url_detail['url'].required_database,
														extensions = [
															'markdown.extensions.extra',
															'markdown.extensions.codehilite',
															'markdown.extensions.toc',
															]
														)
	context_url_detail['url'].required_api =  markdown.markdown(context_url_detail['url'].required_api,
														extensions = [
															'markdown.extensions.extra',
															'markdown.extensions.codehilite',
															'markdown.extensions.toc',
															]
														)
	return render(request, 'services/url_detail.html', context_url_detail)

class UrlDetailView(LoginRequiredMixin, DetailView):

	model = models.Server_URLs
	template_name = "services/url_detail.html"
	context_object_name = "url"

	def get_object(self, queryset=None):
		url = super(UrlDetailView, self).get_object(queryset=queryset)
		url.required_database = markdown.markdown(url.required_database,
													extensions = [
														'markdown.extensions.extra',
														'markdown.extensions.codehilite',
														'markdown.extensions.toc',
														]
													)
		url.required_api = markdown.markdown(url.required_api,
													extensions = [
														'markdown.extensions.extra',
														'markdown.extensions.codehilite',
														'markdown.extensions.toc',
														]
													)
		url.temp = "testinfo"
		return url

	def get_context_data(self, **kwargs):
		context_url_detail = super(UrlDetailView, self).get_context_data(**kwargs)
		context_url_detail['section'] = 'url'
		return context_url_detail

@login_required
def search(request):
	q = request.GET.get('q')
	context_search = {}
	context_search['section'] = 'url'
	context_search['error_msg'] = ''

	if not q:
		context_search[error_msg] = '请输入关键词'
		return render(request, 'services/url.html', context_search)

	# icontains为不区分大小写，contains则区分大小写
	context_search['url_list'] = models.Server_URLs.objects.filter(Q(url__icontains=q) | Q(required_api__icontains=q))
	return render(request, 'services/url.html', context_search)

class ElasticsearchView(LoginRequiredMixin, ListView, PaginationData):

	model = models.Elasticsearch_Node
	template_name = "services/elasticsearch.html"
	#context_object_name = "ela"
	paginate_by = 15

	def get_context_data(self, **kwargs):
		context_elasticsearch = super(ElasticsearchView, self).get_context_data(**kwargs)
		context_elasticsearch['section'] = 'url'
		context_elasticsearch['error_msg'] = ''
		#context_elasticsearch['node_ip'] = models.Elasticsearch_Node.objects.all().values("IP_Address")
		#context_elasticsearch['node_name'] = models.Elasticsearch_Node.objects.all().values("Node_Name")
		logger.info("ElasticsearchView-logging-1")
		node_ip_list = models.Elasticsearch_Node.objects.all().values("IP_Address")
		logger.info(node_ip_list)
		logger.info("ElasticsearchView-logging-2")
		node_name_list = models.Elasticsearch_Node.objects.all().values("Node_Name")
		logger.info(node_name_list)
		context_elasticsearch['nodeinfo'] = node_ip_list
		node_ip_list_length = len(node_ip_list)
		node_name_list_length = len(node_name_list)

		if node_ip_list_length == node_name_list_length:
			logger.info("data match")
			i = 0
			while i < node_ip_list_length:
				context_elasticsearch['nodeinfo'][i].update(node_name_list[i])
				i += 1
			logger.info("increase data complete")
		else:
			logger.info("data match failed")

		logger.info("ElasticsearchView-logging-3")
		logger.info(context_elasticsearch['nodeinfo'])

		
		for k in context_elasticsearch['nodeinfo']:
			elasticsearch_host = k['IP_Address']
			elasticsearch_node_name = k['Node_Name']
			k.update(self.Elasticsearchinfo_Collect(elasticsearch_host, elasticsearch_node_name))
		
		# test
		#context_elasticsearch['temp'] = self.Elasticsearchinfo_Collect("10.181.57.57", "10.181.57.57")
		#logger.info("ElasticsearchView-logging-4")
		#logger.info(context_elasticsearch['temp'])

		logger.info("ElasticsearchView-logging-5")
		logger.info(context_elasticsearch['nodeinfo'])
		return context_elasticsearch

	def Elasticsearchinfo_Collect(self, elasticsearch_host, elasticsearch_node_name, elasticsearch_port="9200"):

		# 配置host和port
		ela_host = Elasticsearch([{'host': elasticsearch_host, 'port': elasticsearch_port}])

		# 获取cluster的health信息
		ela_cluster_health = ela_host.cluster.health()
		
		# 获取nodes的info信息
		ela_nodes_simple_info = ela_host.nodes.info(node_id=elasticsearch_node_name)
		# 获取nodes对应的uid
		ela_nodes_uid = "".join(list(ela_nodes_simple_info["nodes"].keys()))
		
		# 获取nodes的stats信息
		ela_nodes_full_info = ela_host.nodes.stats(node_id=elasticsearch_node_name)
		
		# 获取fs相关信息
		ela_nodes_fs = ela_nodes_full_info["nodes"][ela_nodes_uid]["fs"]
		ela_nodes_fs["total"]["total_in_bytes"] = round(ela_nodes_fs["total"]["total_in_bytes"]/1024/1024/1024, 2)
		ela_nodes_fs["total"]["available_in_bytes"] = round(ela_nodes_fs["total"]["available_in_bytes"]/1024/1024/1024, 2)
		
		# 获取CPU相关信息
		ela_nodes_cpu = ela_nodes_full_info["nodes"][ela_nodes_uid]["process"]

		# 获取JVM相关信息
		ela_nodes_jvm = ela_nodes_full_info["nodes"][ela_nodes_uid]["jvm"]
		ela_nodes_jvm["others"] = ela_nodes_simple_info["nodes"][ela_nodes_uid]["jvm"]

		# 获取indices相关信息
		ela_nodes_indices = ela_nodes_full_info["nodes"][ela_nodes_uid]["indices"]
		ela_nodes_indices['search']['query_latency'] = round(ela_nodes_indices['search']['query_time_in_millis'] / ela_nodes_indices['search']['query_total'], 2)
		ela_nodes_indices['search']['fetch_latency'] = round(ela_nodes_indices['search']['fetch_time_in_millis'] / ela_nodes_indices['search']['fetch_total'], 2)

		ela_collection = {
						'elasticsearch_cluster_health': ela_cluster_health,
						'elasticsearch_nodes_uid': ela_nodes_uid,
						'elasticsearch_node_info_fs': ela_nodes_fs,
						'elasticsearch_node_info_cpu': ela_nodes_cpu,
						'elasticsearch_node_info_jvm': ela_nodes_jvm,
						'elasticsearch_node_info_indices': ela_nodes_indices,
		}

		return ela_collection
