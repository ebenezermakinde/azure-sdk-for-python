# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .job_properties import JobProperties


class USqlJobProperties(JobProperties):
    """U-SQL job properties used when retrieving U-SQL jobs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param runtime_version: The runtime version of the Data Lake Analytics
     engine to use for the specific type of job being run.
    :type runtime_version: str
    :param script: Required. The script to run. Please note that the maximum
     script size is 3 MB.
    :type script: str
    :param type: Required. Constant filled by server.
    :type type: str
    :ivar resources: The list of resources that are required by the job.
    :vartype resources:
     list[~azure.mgmt.datalake.analytics.job.models.JobResource]
    :param statistics: The job specific statistics.
    :type statistics: ~azure.mgmt.datalake.analytics.job.models.JobStatistics
    :param debug_data: The job specific debug data locations.
    :type debug_data: ~azure.mgmt.datalake.analytics.job.models.JobDataPath
    :ivar diagnostics: The diagnostics for the job.
    :vartype diagnostics:
     list[~azure.mgmt.datalake.analytics.job.models.Diagnostics]
    :ivar algebra_file_path: The algebra file path after the job has
     completed.
    :vartype algebra_file_path: str
    :ivar total_compilation_time: The total time this job spent compiling.
     This value should not be set by the user and will be ignored if it is.
    :vartype total_compilation_time: timedelta
    :ivar total_queued_time: The total time this job spent queued. This value
     should not be set by the user and will be ignored if it is.
    :vartype total_queued_time: timedelta
    :ivar total_running_time: The total time this job spent executing. This
     value should not be set by the user and will be ignored if it is.
    :vartype total_running_time: timedelta
    :ivar total_paused_time: The total time this job spent paused. This value
     should not be set by the user and will be ignored if it is.
    :vartype total_paused_time: timedelta
    :ivar root_process_node_id: The ID used to identify the job manager
     coordinating job execution. This value should not be set by the user and
     will be ignored if it is.
    :vartype root_process_node_id: str
    :ivar yarn_application_id: The ID used to identify the yarn application
     executing the job. This value should not be set by the user and will be
     ignored if it is.
    :vartype yarn_application_id: str
    :ivar yarn_application_time_stamp: The timestamp (in ticks) for the yarn
     application executing the job. This value should not be set by the user
     and will be ignored if it is.
    :vartype yarn_application_time_stamp: long
    :ivar compile_mode: The specific compilation mode for the job used during
     execution. If this is not specified during submission, the server will
     determine the optimal compilation mode. Possible values include:
     'Semantic', 'Full', 'SingleBox'
    :vartype compile_mode: str or
     ~azure.mgmt.datalake.analytics.job.models.CompileMode
    """

    _validation = {
        'script': {'required': True},
        'type': {'required': True},
        'resources': {'readonly': True},
        'diagnostics': {'readonly': True},
        'algebra_file_path': {'readonly': True},
        'total_compilation_time': {'readonly': True},
        'total_queued_time': {'readonly': True},
        'total_running_time': {'readonly': True},
        'total_paused_time': {'readonly': True},
        'root_process_node_id': {'readonly': True},
        'yarn_application_id': {'readonly': True},
        'yarn_application_time_stamp': {'readonly': True},
        'compile_mode': {'readonly': True},
    }

    _attribute_map = {
        'runtime_version': {'key': 'runtimeVersion', 'type': 'str'},
        'script': {'key': 'script', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[JobResource]'},
        'statistics': {'key': 'statistics', 'type': 'JobStatistics'},
        'debug_data': {'key': 'debugData', 'type': 'JobDataPath'},
        'diagnostics': {'key': 'diagnostics', 'type': '[Diagnostics]'},
        'algebra_file_path': {'key': 'algebraFilePath', 'type': 'str'},
        'total_compilation_time': {'key': 'totalCompilationTime', 'type': 'duration'},
        'total_queued_time': {'key': 'totalQueuedTime', 'type': 'duration'},
        'total_running_time': {'key': 'totalRunningTime', 'type': 'duration'},
        'total_paused_time': {'key': 'totalPausedTime', 'type': 'duration'},
        'root_process_node_id': {'key': 'rootProcessNodeId', 'type': 'str'},
        'yarn_application_id': {'key': 'yarnApplicationId', 'type': 'str'},
        'yarn_application_time_stamp': {'key': 'yarnApplicationTimeStamp', 'type': 'long'},
        'compile_mode': {'key': 'compileMode', 'type': 'CompileMode'},
    }

    def __init__(self, **kwargs):
        super(USqlJobProperties, self).__init__(**kwargs)
        self.resources = None
        self.statistics = kwargs.get('statistics', None)
        self.debug_data = kwargs.get('debug_data', None)
        self.diagnostics = None
        self.algebra_file_path = None
        self.total_compilation_time = None
        self.total_queued_time = None
        self.total_running_time = None
        self.total_paused_time = None
        self.root_process_node_id = None
        self.yarn_application_id = None
        self.yarn_application_time_stamp = None
        self.compile_mode = None
        self.type = 'USql'