# looker_client_31.DashboardApi

All URIs are relative to *https://saleseng.dev.looker.com:19999/api/3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_dashboards**](DashboardApi.md#all_dashboards) | **GET** /dashboards | Get All Dashboards
[**create_dashboard**](DashboardApi.md#create_dashboard) | **POST** /dashboards | Create Dashboard
[**create_dashboard_element**](DashboardApi.md#create_dashboard_element) | **POST** /dashboard_elements | Create DashboardElement
[**create_dashboard_filter**](DashboardApi.md#create_dashboard_filter) | **POST** /dashboard_filters | Create Dashboard Filter
[**create_dashboard_layout**](DashboardApi.md#create_dashboard_layout) | **POST** /dashboard_layouts | Create DashboardLayout
[**dashboard**](DashboardApi.md#dashboard) | **GET** /dashboards/{dashboard_id} | Get Dashboard
[**dashboard_dashboard_elements**](DashboardApi.md#dashboard_dashboard_elements) | **GET** /dashboards/{dashboard_id}/dashboard_elements | Get All DashboardElements
[**dashboard_dashboard_filters**](DashboardApi.md#dashboard_dashboard_filters) | **GET** /dashboards/{dashboard_id}/dashboard_filters | Get All Dashboard Filters
[**dashboard_dashboard_layouts**](DashboardApi.md#dashboard_dashboard_layouts) | **GET** /dashboards/{dashboard_id}/dashboard_layouts | Get All DashboardLayouts
[**dashboard_element**](DashboardApi.md#dashboard_element) | **GET** /dashboard_elements/{dashboard_element_id} | Get DashboardElement
[**dashboard_filter**](DashboardApi.md#dashboard_filter) | **GET** /dashboard_filters/{dashboard_filter_id} | Get Dashboard Filter
[**dashboard_layout**](DashboardApi.md#dashboard_layout) | **GET** /dashboard_layouts/{dashboard_layout_id} | Get DashboardLayout
[**dashboard_layout_component**](DashboardApi.md#dashboard_layout_component) | **GET** /dashboard_layout_components/{dashboard_layout_component_id} | Get DashboardLayoutComponent
[**dashboard_layout_dashboard_layout_components**](DashboardApi.md#dashboard_layout_dashboard_layout_components) | **GET** /dashboard_layouts/{dashboard_layout_id}/dashboard_layout_components | Get All DashboardLayoutComponents
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **DELETE** /dashboards/{dashboard_id} | Delete Dashboard
[**delete_dashboard_element**](DashboardApi.md#delete_dashboard_element) | **DELETE** /dashboard_elements/{dashboard_element_id} | Delete DashboardElement
[**delete_dashboard_filter**](DashboardApi.md#delete_dashboard_filter) | **DELETE** /dashboard_filters/{dashboard_filter_id} | Delete Dashboard Filter
[**delete_dashboard_layout**](DashboardApi.md#delete_dashboard_layout) | **DELETE** /dashboard_layouts/{dashboard_layout_id} | Delete DashboardLayout
[**search_dashboard_elements**](DashboardApi.md#search_dashboard_elements) | **GET** /dashboard_elements/search | Get DashboardElement
[**search_dashboards**](DashboardApi.md#search_dashboards) | **GET** /dashboards/search | Search Dashboards
[**update_dashboard**](DashboardApi.md#update_dashboard) | **PATCH** /dashboards/{dashboard_id} | Update Dashboard
[**update_dashboard_element**](DashboardApi.md#update_dashboard_element) | **PATCH** /dashboard_elements/{dashboard_element_id} | Update DashboardElement
[**update_dashboard_filter**](DashboardApi.md#update_dashboard_filter) | **PATCH** /dashboard_filters/{dashboard_filter_id} | Update Dashboard Filter
[**update_dashboard_layout**](DashboardApi.md#update_dashboard_layout) | **PATCH** /dashboard_layouts/{dashboard_layout_id} | Update DashboardLayout
[**update_dashboard_layout_component**](DashboardApi.md#update_dashboard_layout_component) | **PATCH** /dashboard_layout_components/{dashboard_layout_component_id} | Update DashboardLayoutComponent


# **all_dashboards**
> list[DashboardBase] all_dashboards(fields=fields)

Get All Dashboards

### Get information about all active dashboards.  Returns an array of **abbreviated dashboard objects**. Dashboards marked as deleted are excluded from this list.  Get the **full details** of a specific dashboard by id with [Dashboard](#!/Dashboard/dashboard)  Find **deleted dashboards** with [Search Dashboards](#!/Dashboard/search_dashboards) 

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get All Dashboards
    api_response = api_instance.all_dashboards(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->all_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DashboardBase]**](DashboardBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard**
> Dashboard create_dashboard(body=body)

Create Dashboard

### Create a dashboard with the specified information  Creates a new dashboard object, returning the dashboard details, including the created id.  **Update** an existing dashboard with [Update Dashboard](#!/Dashboard/update_dashboard)  **Permanently delete** an existing dashboard with [Delete Dashboard](#!/Dashboard/delete_dashboard) 

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
body = looker_client_31.Dashboard() # Dashboard | Dashboard (optional)

try:
    # Create Dashboard
    api_response = api_instance.create_dashboard(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| Dashboard | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_element**
> DashboardElement create_dashboard_element(body=body, fields=fields)

Create DashboardElement

### Create a dashboard element on the dashboard with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
body = looker_client_31.DashboardElement() # DashboardElement | DashboardElement (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Create DashboardElement
    api_response = api_instance.create_dashboard_element(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboard_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DashboardElement**](DashboardElement.md)| DashboardElement | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardElement**](DashboardElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_filter**
> DashboardFilter create_dashboard_filter(body, fields=fields)

Create Dashboard Filter

### Create a dashboard filter on the dashboard with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
body = looker_client_31.CreateDashboardFilter() # CreateDashboardFilter | Dashboard Filter
fields = 'fields_example' # str | Requested fields (optional)

try:
    # Create Dashboard Filter
    api_response = api_instance.create_dashboard_filter(body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboard_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDashboardFilter**](CreateDashboardFilter.md)| Dashboard Filter | 
 **fields** | **str**| Requested fields | [optional] 

### Return type

[**DashboardFilter**](DashboardFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_layout**
> DashboardLayout create_dashboard_layout(body=body, fields=fields)

Create DashboardLayout

### Create a dashboard layout on the dashboard with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
body = looker_client_31.DashboardLayout() # DashboardLayout | DashboardLayout (optional)
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Create DashboardLayout
    api_response = api_instance.create_dashboard_layout(body=body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboard_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DashboardLayout**](DashboardLayout.md)| DashboardLayout | [optional] 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardLayout**](DashboardLayout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard**
> Dashboard dashboard(dashboard_id, fields=fields)

Get Dashboard

### Get information about the dashboard with the specified id  Returns the full details of the identified dashboard object  Get a **summary list** of all active dashboards with [All Dashboards](#!/Dashboard/all_dashboards)  **Search** for dashboards with [Search Dashboards](#!/Dashboard/search_dashboards) 

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get Dashboard
    api_response = api_instance.dashboard(dashboard_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_dashboard_elements**
> list[DashboardElement] dashboard_dashboard_elements(dashboard_id, fields=fields)

Get All DashboardElements

### Get information about all the dashboard elements on a dashboard with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get All DashboardElements
    api_response = api_instance.dashboard_dashboard_elements(dashboard_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_dashboard_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DashboardElement]**](DashboardElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_dashboard_filters**
> list[DashboardFilter] dashboard_dashboard_filters(dashboard_id, fields=fields)

Get All Dashboard Filters

### Get information about all the dashboard filters on a dashboard with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get All Dashboard Filters
    api_response = api_instance.dashboard_dashboard_filters(dashboard_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_dashboard_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DashboardFilter]**](DashboardFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_dashboard_layouts**
> list[DashboardLayout] dashboard_dashboard_layouts(dashboard_id, fields=fields)

Get All DashboardLayouts

### Get information about all the dashboard elemnts on a dashboard with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get All DashboardLayouts
    api_response = api_instance.dashboard_dashboard_layouts(dashboard_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_dashboard_layouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DashboardLayout]**](DashboardLayout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_element**
> DashboardElement dashboard_element(dashboard_element_id, fields=fields)

Get DashboardElement

### Get information about the dashboard element with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_element_id = 'dashboard_element_id_example' # str | Id of dashboard element
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get DashboardElement
    api_response = api_instance.dashboard_element(dashboard_element_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_element_id** | **str**| Id of dashboard element | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardElement**](DashboardElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_filter**
> DashboardFilter dashboard_filter(dashboard_filter_id, fields=fields)

Get Dashboard Filter

### Get information about the dashboard filters with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_filter_id = 'dashboard_filter_id_example' # str | Id of dashboard filters
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get Dashboard Filter
    api_response = api_instance.dashboard_filter(dashboard_filter_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_filter_id** | **str**| Id of dashboard filters | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardFilter**](DashboardFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_layout**
> DashboardLayout dashboard_layout(dashboard_layout_id, fields=fields)

Get DashboardLayout

### Get information about the dashboard layouts with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_layout_id = 'dashboard_layout_id_example' # str | Id of dashboard layouts
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get DashboardLayout
    api_response = api_instance.dashboard_layout(dashboard_layout_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_layout_id** | **str**| Id of dashboard layouts | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardLayout**](DashboardLayout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_layout_component**
> DashboardLayoutComponent dashboard_layout_component(dashboard_layout_component_id, fields=fields)

Get DashboardLayoutComponent

### Get information about the dashboard elements with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_layout_component_id = 'dashboard_layout_component_id_example' # str | Id of dashboard layout component
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get DashboardLayoutComponent
    api_response = api_instance.dashboard_layout_component(dashboard_layout_component_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_layout_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_layout_component_id** | **str**| Id of dashboard layout component | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardLayoutComponent**](DashboardLayoutComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_layout_dashboard_layout_components**
> list[DashboardLayoutComponent] dashboard_layout_dashboard_layout_components(dashboard_layout_id, fields=fields)

Get All DashboardLayoutComponents

### Get information about all the dashboard layout components for a dashboard layout with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_layout_id = 'dashboard_layout_id_example' # str | Id of dashboard layout component
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Get All DashboardLayoutComponents
    api_response = api_instance.dashboard_layout_dashboard_layout_components(dashboard_layout_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_layout_dashboard_layout_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_layout_id** | **str**| Id of dashboard layout component | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**list[DashboardLayoutComponent]**](DashboardLayoutComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> str delete_dashboard(dashboard_id)

Delete Dashboard

### Delete the dashboard with the specified id  Permanently **deletes** a dashboard. (The dashboard cannot be recovered after this operation.)  \"Soft\" delete or hide a dashboard by setting its `deleted` status to `True` with [Update Dashboard](#!/Dashboard/update_dashboard).  Note: When a dashboard is deleted in the UI, it is soft deleted. Use this API call to permanently remove it, if desired. 

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard

try:
    # Delete Dashboard
    api_response = api_instance.delete_dashboard(dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_element**
> str delete_dashboard_element(dashboard_element_id)

Delete DashboardElement

### Delete a dashboard element with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_element_id = 'dashboard_element_id_example' # str | Id of dashboard element

try:
    # Delete DashboardElement
    api_response = api_instance.delete_dashboard_element(dashboard_element_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->delete_dashboard_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_element_id** | **str**| Id of dashboard element | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_filter**
> str delete_dashboard_filter(dashboard_filter_id)

Delete Dashboard Filter

### Delete a dashboard filter with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_filter_id = 'dashboard_filter_id_example' # str | Id of dashboard filter

try:
    # Delete Dashboard Filter
    api_response = api_instance.delete_dashboard_filter(dashboard_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->delete_dashboard_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_filter_id** | **str**| Id of dashboard filter | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_layout**
> str delete_dashboard_layout(dashboard_layout_id)

Delete DashboardLayout

### Delete a dashboard layout with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_layout_id = 'dashboard_layout_id_example' # str | Id of dashboard layout

try:
    # Delete DashboardLayout
    api_response = api_instance.delete_dashboard_layout(dashboard_layout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->delete_dashboard_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_layout_id** | **str**| Id of dashboard layout | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboard_elements**
> list[DashboardElement] search_dashboard_elements(fields=fields, look_id=look_id, dashboard_id=dashboard_id, title=title)

Get DashboardElement

### Get information on dashboard look relations for a set of look ids.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
fields = 'fields_example' # str | Requested fields. (optional)
look_id = 789 # int | Id of look (optional)
dashboard_id = 789 # int | Id of dashboard (optional)
title = 'title_example' # str | Title of element (optional)

try:
    # Get DashboardElement
    api_response = api_instance.search_dashboard_elements(fields=fields, look_id=look_id, dashboard_id=dashboard_id, title=title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->search_dashboard_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **look_id** | **int**| Id of look | [optional] 
 **dashboard_id** | **int**| Id of dashboard | [optional] 
 **title** | **str**| Title of element | [optional] 

### Return type

[**list[DashboardElement]**](DashboardElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboards**
> list[Dashboard] search_dashboards(fields=fields, id=id, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, title=title, description=description, content_favorite_id=content_favorite_id, space_id=space_id, deleted=deleted, user_id=user_id, view_count=view_count)

Search Dashboards

### Search all dashboards for matching criteria.  Returns an **array of dashboard objects** that match the specified search criteria.  The parameters `limit`, and `offset` are recommended for \"paging\" the returned results.  Get a **single dashboard** by id with [Dashboard](#!/Dashboard/dashboard) 

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
fields = 'fields_example' # str | Requested fields. (optional)
id = 789 # int | Match dashboard id. (optional)
page = 789 # int | Requested page. (optional)
per_page = 789 # int | Results per page. (optional)
limit = 789 # int | Number of results to return. (used with offset and takes priority over page and per_page) (optional)
offset = 789 # int | Number of results to skip before returning any. (used with limit and takes priority over page and per_page) (optional)
sorts = 'sorts_example' # str | Fields to sort by. (optional)
title = 'title_example' # str | Match Dashboard title. (optional)
description = 'description_example' # str | Match Dashboard description. (optional)
content_favorite_id = 789 # int | Filter on a content favorite id. (optional)
space_id = 'space_id_example' # str | Filter on a particular space. (optional)
deleted = 'deleted_example' # str | Filter on dashboards deleted status. (optional)
user_id = 'user_id_example' # str | Filter on dashboards created by a particular user. (optional)
view_count = 'view_count_example' # str | Filter on a particular value of view_count (optional)

try:
    # Search Dashboards
    api_response = api_instance.search_dashboards(fields=fields, id=id, page=page, per_page=per_page, limit=limit, offset=offset, sorts=sorts, title=title, description=description, content_favorite_id=content_favorite_id, space_id=space_id, deleted=deleted, user_id=user_id, view_count=view_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->search_dashboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Requested fields. | [optional] 
 **id** | **int**| Match dashboard id. | [optional] 
 **page** | **int**| Requested page. | [optional] 
 **per_page** | **int**| Results per page. | [optional] 
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional] 
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional] 
 **sorts** | **str**| Fields to sort by. | [optional] 
 **title** | **str**| Match Dashboard title. | [optional] 
 **description** | **str**| Match Dashboard description. | [optional] 
 **content_favorite_id** | **int**| Filter on a content favorite id. | [optional] 
 **space_id** | **str**| Filter on a particular space. | [optional] 
 **deleted** | **str**| Filter on dashboards deleted status. | [optional] 
 **user_id** | **str**| Filter on dashboards created by a particular user. | [optional] 
 **view_count** | **str**| Filter on a particular value of view_count | [optional] 

### Return type

[**list[Dashboard]**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(dashboard_id, body)

Update Dashboard

### Update the dashboard with the specified id  Changes simple (scalar) properties of the dashboard.  Change dashboard **elements** with [Update Dashboard Element](#!/Dashboard/update_dashboard_element)  Change dashboard **filters** with [Update Dashboard Filter](#!/Dashboard/update_dashboard_filter)  Change dashboard **layouts** with [Update Dashboard Layout](#!/Dashboard/update_dashboard_layout)  Change dashboard **layout components** with [Update Dashboard Layout Component](#!/Dashboard/update_dashboard_layout_components) 

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_id = 'dashboard_id_example' # str | Id of dashboard
body = looker_client_31.Dashboard() # Dashboard | Dashboard

try:
    # Update Dashboard
    api_response = api_instance.update_dashboard(dashboard_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| Id of dashboard | 
 **body** | [**Dashboard**](Dashboard.md)| Dashboard | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_element**
> DashboardElement update_dashboard_element(dashboard_element_id, body, fields=fields)

Update DashboardElement

### Update the dashboard element with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_element_id = 'dashboard_element_id_example' # str | Id of dashboard element
body = looker_client_31.DashboardElement() # DashboardElement | DashboardElement
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Update DashboardElement
    api_response = api_instance.update_dashboard_element(dashboard_element_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->update_dashboard_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_element_id** | **str**| Id of dashboard element | 
 **body** | [**DashboardElement**](DashboardElement.md)| DashboardElement | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardElement**](DashboardElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_filter**
> DashboardFilter update_dashboard_filter(dashboard_filter_id, body, fields=fields)

Update Dashboard Filter

### Update the dashboard filter with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_filter_id = 'dashboard_filter_id_example' # str | Id of dashboard filter
body = looker_client_31.DashboardFilter() # DashboardFilter | Dashboard Filter
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Update Dashboard Filter
    api_response = api_instance.update_dashboard_filter(dashboard_filter_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->update_dashboard_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_filter_id** | **str**| Id of dashboard filter | 
 **body** | [**DashboardFilter**](DashboardFilter.md)| Dashboard Filter | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardFilter**](DashboardFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_layout**
> DashboardLayout update_dashboard_layout(dashboard_layout_id, body, fields=fields)

Update DashboardLayout

### Update the dashboard layout with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_layout_id = 'dashboard_layout_id_example' # str | Id of dashboard layout
body = looker_client_31.DashboardLayout() # DashboardLayout | DashboardLayout
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Update DashboardLayout
    api_response = api_instance.update_dashboard_layout(dashboard_layout_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->update_dashboard_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_layout_id** | **str**| Id of dashboard layout | 
 **body** | [**DashboardLayout**](DashboardLayout.md)| DashboardLayout | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardLayout**](DashboardLayout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_layout_component**
> DashboardLayoutComponent update_dashboard_layout_component(dashboard_layout_component_id, body, fields=fields)

Update DashboardLayoutComponent

### Update the dashboard element with a specific id.

### Example
```python
from __future__ import print_function
import time
import looker_client_31
from looker_client_31.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = looker_client_31.DashboardApi()
dashboard_layout_component_id = 'dashboard_layout_component_id_example' # str | Id of dashboard layout component
body = looker_client_31.DashboardLayoutComponent() # DashboardLayoutComponent | DashboardLayoutComponent
fields = 'fields_example' # str | Requested fields. (optional)

try:
    # Update DashboardLayoutComponent
    api_response = api_instance.update_dashboard_layout_component(dashboard_layout_component_id, body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->update_dashboard_layout_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_layout_component_id** | **str**| Id of dashboard layout component | 
 **body** | [**DashboardLayoutComponent**](DashboardLayoutComponent.md)| DashboardLayoutComponent | 
 **fields** | **str**| Requested fields. | [optional] 

### Return type

[**DashboardLayoutComponent**](DashboardLayoutComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

