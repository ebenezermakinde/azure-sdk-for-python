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

from .article import Article


class NewsArticle(Article):
    """Defines a news article.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image:
     ~azure.cognitiveservices.search.newssearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider:
     list[~azure.cognitiveservices.search.newssearch.models.Thing]
    :ivar date_published: The date on which the CreativeWork was published.
    :vartype date_published: str
    :ivar video: A video of the item.
    :vartype video:
     ~azure.cognitiveservices.search.newssearch.models.VideoObject
    :ivar word_count: The number of words in the text of the Article.
    :vartype word_count: int
    :ivar category: The news category that the article belongs to. For
     example, Sports. If the news category cannot be determined, the article
     does not include this field.
    :vartype category: str
    :ivar headline: A Boolean value that indicates whether the news article is
     a headline. If true, the article is a headline. The article includes this
     field only for news categories requests that do not specify the category
     query parameter.
    :vartype headline: bool
    :ivar clustered_articles: A list of related news articles.
    :vartype clustered_articles:
     list[~azure.cognitiveservices.search.newssearch.models.NewsArticle]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'date_published': {'readonly': True},
        'video': {'readonly': True},
        'word_count': {'readonly': True},
        'category': {'readonly': True},
        'headline': {'readonly': True},
        'clustered_articles': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'date_published': {'key': 'datePublished', 'type': 'str'},
        'video': {'key': 'video', 'type': 'VideoObject'},
        'word_count': {'key': 'wordCount', 'type': 'int'},
        'category': {'key': 'category', 'type': 'str'},
        'headline': {'key': 'headline', 'type': 'bool'},
        'clustered_articles': {'key': 'clusteredArticles', 'type': '[NewsArticle]'},
    }

    def __init__(self, **kwargs) -> None:
        super(NewsArticle, self).__init__(**kwargs)
        self.category = None
        self.headline = None
        self.clustered_articles = None
        self._type = 'NewsArticle'