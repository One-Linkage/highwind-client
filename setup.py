# coding: utf-8

"""
    Highwind AI Solution - Document Verifier

    The Highwind AI Document Verifier provides an easy way to analyse financial related documents (financial statements, purchase orders, etc) as an API service for clients.   ## Flow `get_upload_url` **-->** `PUT` presigned URL **-->** Highwind AI Solution analyses `pdf` file **-->** `get_results`  ## Endpoints ### 1. Upload Document: get_upload_url/{object}?document-type={type} - This endpoint generates two items:   - A presigned URL required to upload the file to our storage system.   - A unique `task_id` which is associated with the presigned URL - You need to use this presigned URL to upload the `pdf` file (currently, only `pdf` files are accepted) for analysis with a `PUT` request    - Content type is `application/pdf`   - Files should be ideally kept under 5mb in size. - `{object}` is a string field which will be the name of the file that is uploaded to the storage system. - `{type}` is the string query parameter that determines the type of document that will be analysed. For example:   - `?document-type=afs` for annual financial statements    - `?document-type=bs` for bank statements    ### 2. Post document to presigned URL using PUT - To use the presigned URL from step 1: Send a PUT request with the curl command. Include the full path to your file and the presigned URL itself. - Command: ```curl -X PUT -T \"/path/to/file\" \"presigned URL\"```    ### 3. Get Results: get_results/{object} - This endpoint returns the summary of the `pdf` file that was uploaded via the presigned URL.   - It takes about 1 - 2 minutes to generate the summary. For larger files it will take more time. It will return `in_progress` while it analysing the `pdf` file. - `{object}` is a string field for you to add the generated `task_id` to look up the associated summary.    `OPTIONS` endpoints are for CORS purposes only.    ### Links 

    The version of the OpenAPI document: 3.0
    Contact: admin@melio.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "highwind-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Highwind AI Solution - Document Verifier",
    author="Melio AI",
    author_email="admin@melio.ai",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Highwind AI Solution - Document Verifier"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    The Highwind AI Document Verifier provides an easy way to analyse financial related documents (financial statements, purchase orders, etc) as an API service for clients.   ## Flow &#x60;get_upload_url&#x60; **--&gt;** &#x60;PUT&#x60; presigned URL **--&gt;** Highwind AI Solution analyses &#x60;pdf&#x60; file **--&gt;** &#x60;get_results&#x60;  ## Endpoints ### 1. Upload Document: get_upload_url/{object}?document-type&#x3D;{type} - This endpoint generates two items:   - A presigned URL required to upload the file to our storage system.   - A unique &#x60;task_id&#x60; which is associated with the presigned URL - You need to use this presigned URL to upload the &#x60;pdf&#x60; file (currently, only &#x60;pdf&#x60; files are accepted) for analysis with a &#x60;PUT&#x60; request    - Content type is &#x60;application/pdf&#x60;   - Files should be ideally kept under 5mb in size. - &#x60;{object}&#x60; is a string field which will be the name of the file that is uploaded to the storage system. - &#x60;{type}&#x60; is the string query parameter that determines the type of document that will be analysed. For example:   - &#x60;?document-type&#x3D;afs&#x60; for annual financial statements    - &#x60;?document-type&#x3D;bs&#x60; for bank statements    ### 2. Post document to presigned URL using PUT - To use the presigned URL from step 1: Send a PUT request with the curl command. Include the full path to your file and the presigned URL itself. - Command: &#x60;&#x60;&#x60;curl -X PUT -T \&quot;/path/to/file\&quot; \&quot;presigned URL\&quot;&#x60;&#x60;&#x60;    ### 3. Get Results: get_results/{object} - This endpoint returns the summary of the &#x60;pdf&#x60; file that was uploaded via the presigned URL.   - It takes about 1 - 2 minutes to generate the summary. For larger files it will take more time. It will return &#x60;in_progress&#x60; while it analysing the &#x60;pdf&#x60; file. - &#x60;{object}&#x60; is a string field for you to add the generated &#x60;task_id&#x60; to look up the associated summary.    &#x60;OPTIONS&#x60; endpoints are for CORS purposes only.    ### Links 
    """,  # noqa: E501
    package_data={"highwind_client": ["py.typed"]},
)
