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

from msrest.serialization import Model


class User(Model):
    """Active Directory user information.

    :param object_id: object Id
    :type object_id: str
    :param object_type: object type
    :type object_type: str
    :param user_principal_name: user principal name
    :type user_principal_name: str
    :param display_name: user display name
    :type display_name: str
    :param sign_in_name: user signIn name
    :type sign_in_name: str
    :param mail: user mail
    :type mail: str
    :param mail_nickname: The mail alias for the user
    :type mail_nickname: str
    """ 

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'sign_in_name': {'key': 'signInName', 'type': 'str'},
        'mail': {'key': 'mail', 'type': 'str'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
    }

    def __init__(self, object_id=None, object_type=None, user_principal_name=None, display_name=None, sign_in_name=None, mail=None, mail_nickname=None):
        self.object_id = object_id
        self.object_type = object_type
        self.user_principal_name = user_principal_name
        self.display_name = display_name
        self.sign_in_name = sign_in_name
        self.mail = mail
        self.mail_nickname = mail_nickname
