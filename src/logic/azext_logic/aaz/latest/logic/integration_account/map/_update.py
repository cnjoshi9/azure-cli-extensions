# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "logic integration-account map update",
)
class Update(AAZCommand):
    """Update an integration account map. If the map is larger than 4 MB, you need to store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the 'contentLink' property value.

    :example: Update map
        az logic integration-account map update -g rg -n map-name --integration-account account-name
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/maps/{}", "2019-05-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.integration_account = AAZStrArg(
            options=["--integration-account"],
            help="The integration account name.",
            required=True,
            id_part="name",
        )
        _args_schema.map_name = AAZStrArg(
            options=["-n", "--name", "--map-name"],
            help="The integration account map name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Map"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Map",
            help="The resource location.",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Map",
            help="The resource tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.content = AAZStrArg(
            options=["--content"],
            arg_group="Properties",
            help="The content.",
            nullable=True,
        )
        _args_schema.content_type = AAZStrArg(
            options=["--content-type"],
            arg_group="Properties",
            help="The content type.",
            nullable=True,
        )
        _args_schema.map_type = AAZStrArg(
            options=["--map-type"],
            arg_group="Properties",
            help="The map type.",
            enum={"Liquid": "Liquid", "NotSpecified": "NotSpecified", "Xslt": "Xslt", "Xslt20": "Xslt20", "Xslt30": "Xslt30"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountMapsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.IntegrationAccountMapsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IntegrationAccountMapsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account,
                    required=True,
                ),
                **self.serialize_url_param(
                    "mapName", self.ctx.args.map_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_integration_account_map_read(cls._schema_on_200)

            return cls._schema_on_200

    class IntegrationAccountMapsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account,
                    required=True,
                ),
                **self.serialize_url_param(
                    "mapName", self.ctx.args.map_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_integration_account_map_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("content", AAZStrType, ".content")
                properties.set_prop("contentType", AAZStrType, ".content_type")
                properties.set_prop("mapType", AAZStrType, ".map_type", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_integration_account_map_read = None

    @classmethod
    def _build_schema_integration_account_map_read(cls, _schema):
        if cls._schema_integration_account_map_read is not None:
            _schema.id = cls._schema_integration_account_map_read.id
            _schema.location = cls._schema_integration_account_map_read.location
            _schema.name = cls._schema_integration_account_map_read.name
            _schema.properties = cls._schema_integration_account_map_read.properties
            _schema.tags = cls._schema_integration_account_map_read.tags
            _schema.type = cls._schema_integration_account_map_read.type
            return

        cls._schema_integration_account_map_read = _schema_integration_account_map_read = AAZObjectType()

        integration_account_map_read = _schema_integration_account_map_read
        integration_account_map_read.id = AAZStrType(
            flags={"read_only": True},
        )
        integration_account_map_read.location = AAZStrType()
        integration_account_map_read.name = AAZStrType(
            flags={"read_only": True},
        )
        integration_account_map_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        integration_account_map_read.tags = AAZDictType()
        integration_account_map_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_integration_account_map_read.properties
        properties.changed_time = AAZStrType(
            serialized_name="changedTime",
            flags={"read_only": True},
        )
        properties.content = AAZStrType()
        properties.content_link = AAZObjectType(
            serialized_name="contentLink",
        )
        properties.content_type = AAZStrType(
            serialized_name="contentType",
        )
        properties.created_time = AAZStrType(
            serialized_name="createdTime",
            flags={"read_only": True},
        )
        properties.map_type = AAZStrType(
            serialized_name="mapType",
            flags={"required": True},
        )
        properties.parameters_schema = AAZObjectType(
            serialized_name="parametersSchema",
        )

        content_link = _schema_integration_account_map_read.properties.content_link
        content_link.content_hash = AAZObjectType(
            serialized_name="contentHash",
        )
        content_link.content_size = AAZIntType(
            serialized_name="contentSize",
            flags={"read_only": True},
        )
        content_link.content_version = AAZStrType(
            serialized_name="contentVersion",
            flags={"read_only": True},
        )
        content_link.uri = AAZStrType()

        content_hash = _schema_integration_account_map_read.properties.content_link.content_hash
        content_hash.algorithm = AAZStrType()
        content_hash.value = AAZStrType()

        parameters_schema = _schema_integration_account_map_read.properties.parameters_schema
        parameters_schema.ref = AAZStrType()

        tags = _schema_integration_account_map_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_integration_account_map_read.id
        _schema.location = cls._schema_integration_account_map_read.location
        _schema.name = cls._schema_integration_account_map_read.name
        _schema.properties = cls._schema_integration_account_map_read.properties
        _schema.tags = cls._schema_integration_account_map_read.tags
        _schema.type = cls._schema_integration_account_map_read.type


__all__ = ["Update"]