# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMError

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class RecommendationMetadataOperations:
    """RecommendationMetadataOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.advisor.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        name: str,
        **kwargs
    ) -> Union["models.MetadataEntity", "models.ARMErrorResponseBody"]:
        """Gets the metadata entity.

        Gets the metadata entity.

        :param name: Name of metadata entity.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MetadataEntity or ARMErrorResponseBody or the result of cls(response)
        :rtype: ~azure.mgmt.advisor.models.MetadataEntity or ~azure.mgmt.advisor.models.ARMErrorResponseBody
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls: ClsType[Union["models.MetadataEntity", "models.ARMErrorResponseBody"]] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2017-04-19"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('MetadataEntity', pipeline_response)

        if response.status_code == 404:
            deserialized = self._deserialize('ARMErrorResponseBody', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Advisor/metadata/{name}'}

    def list(
        self,
        **kwargs
    ) -> "models.MetadataEntityListResult":
        """Gets the list of metadata entities.

        Gets the list of metadata entities.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MetadataEntityListResult or the result of cls(response)
        :rtype: ~azure.mgmt.advisor.models.MetadataEntityListResult
        :raises: ~azure.mgmt.core.ARMError
        """
        cls: ClsType["models.MetadataEntityListResult"] = kwargs.pop('cls', None)
        error_map = kwargs.pop('error_map', {})
        api_version = "2017-04-19"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('MetadataEntityListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise ARMError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/providers/Microsoft.Advisor/metadata'}