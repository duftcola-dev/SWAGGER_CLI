# NAME

WWW::SwaggerClient::Role - a Moose role for the Swagger Petstore

This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

# VERSION

Automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PerlClientCodegen

## A note on Moose

This role is the only component of the library that uses Moose. See
WWW::SwaggerClient::ApiFactory for non-Moosey usage.

# SYNOPSIS

The Perl Swagger Codegen project builds a library of Perl modules to interact with
a web service defined by a OpenAPI Specification. See below for how to build the
library.

This module provides an interface to the generated library. All the classes,
objects, and methods (well, not quite \*all\*, see below) are flattened into this
role.

        package MyApp;
        use Moose;
        with 'WWW::SwaggerClient::Role';

        package main;

        my $api = MyApp->new({ tokens => $tokens });

        my $pet = $api->get_pet_by_id(pet_id => $pet_id);


## Structure of the library

The library consists of a set of API classes, one for each endpoint. These APIs
implement the method calls available on each endpoint.

Additionally, there is a set of "object" classes, which represent the objects
returned by and sent to the methods on the endpoints.

An API factory class is provided, which builds instances of each endpoint API.

This Moose role flattens all the methods from the endpoint APIs onto the consuming
class. It also provides methods to retrieve the endpoint API objects, and the API
factory object, should you need it.

For documentation of all these methods, see AUTOMATIC DOCUMENTATION below.

## Configuring authentication

In the normal case, the OpenAPI Spec will describe what parameters are
required and where to put them. You just need to supply the tokens.

    my $tokens = {
        # basic
        username => $username,
        password => $password,

        # oauth
        access_token => $oauth_token,

        # keys
        $some_key => { token => $token,
                       prefix => $prefix,
                       in => $in,             # 'head||query',
                       },

        $another => { token => $token,
                      prefix => $prefix,
                      in => $in,              # 'head||query',
                      },
        ...,

        };

        my $api = MyApp->new({ tokens => $tokens });

Note these are all optional, as are `prefix` and `in`, and depend on the API
you are accessing. Usually `prefix` and `in` will be determined by the code generator from
the spec and you will not need to set them at run time. If not, `in` will
default to 'head' and `prefix` to the empty string.

The tokens will be placed in a L<WWW::SwaggerClient::Configuration> instance
as follows, but you don't need to know about this.

- `$cfg->{username}`

    String. The username for basic auth.

- `$cfg->{password}`

    String. The password for basic auth.

- `$cfg->{api_key}`

    Hashref. Keyed on the name of each key (there can be multiple tokens).

            $cfg->{api_key} = {
                    secretKey => 'aaaabbbbccccdddd',
                    anotherKey => '1111222233334444',
                    };

- `$cfg->{api_key_prefix}`

    Hashref. Keyed on the name of each key (there can be multiple tokens). Note not
    all api keys require a prefix.

            $cfg->{api_key_prefix} = {
                    secretKey => 'string',
                    anotherKey => 'same or some other string',
                    };

- `$cfg->{access_token}`

    String. The OAuth access token.

# METHODS

## `base_url`

The generated code has the `base_url` already set as a default value. This method
returns the current value of `base_url`.

## `api_factory`

Returns an API factory object. You probably won't need to call this directly.

        $self->api_factory('Pet'); # returns a WWW::SwaggerClient::PetApi instance

        $self->pet_api;            # the same

# MISSING METHODS

Most of the methods on the API are delegated to individual endpoint API objects
(e.g. Pet API, Store API, User API etc). Where different endpoint APIs use the
same method name (e.g. `new()`), these methods can't be delegated. So you need
to call `$api->pet_api->new()`.

In principle, every API is susceptible to the presence of a few, random, undelegatable
method names. In practice, because of the way method names are constructed, it's
unlikely in general that any methods will be undelegatable, except for:

        new()
        class_documentation()
        method_documentation()

To call these methods, you need to get a handle on the relevant object, either
by calling `$api->foo_api` or by retrieving an object, e.g.
`$api->get_pet_by_id(pet_id => $pet_id)`. They are class methods, so
you could also call them on class names.

# BUILDING YOUR LIBRARY

See the homepage `https://github.com/swagger-api/swagger-codegen` for full details.
But briefly, clone the git repository, build the codegen codebase, set up your build
config file, then run the API build script. You will need git, Java 7 or 8 and Apache
maven 3.0.3 or better already installed.

The config file should specify the project name for the generated library:

        {"moduleName":"WWW::MyProjectName"}

Your library files will be built under `WWW::MyProjectName`.

          $ git clone https://github.com/swagger-api/swagger-codegen.git
          $ cd swagger-codegen
          $ mvn package
          $ java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
    -i [URL or file path to JSON swagger API spec] \
    -l perl \
    -c /path/to/config/file.json \
    -o /path/to/output/folder

Bang, all done. Run the `autodoc` script in the `bin` directory to see the API
you just built.

# AUTOMATIC DOCUMENTATION

You can print out a summary of the generated API by running the included
`autodoc` script in the `bin` directory of your generated library. A few
output formats are supported:

          Usage: autodoc [OPTION]

    -w           wide format (default)
    -n           narrow format
    -p           POD format
    -H           HTML format
    -m           Markdown format
    -h           print this help message
    -c           your application class


The `-c` option allows you to load and inspect your own application. A dummy
namespace is used if you don't supply your own class.

# DOCUMENTATION FROM THE OpenAPI Spec

Additional documentation for each class and method may be provided by the Swagger
spec. If so, this is available via the `class_documentation()` and
`method_documentation()` methods on each generated object class, and the
`method_documentation()` method on the endpoint API classes:

        my $cmdoc = $api->pet_api->method_documentation->{$method_name};

        my $odoc = $api->get_pet_by_id->(pet_id => $pet_id)->class_documentation;
        my $omdoc = $api->get_pet_by_id->(pet_id => $pet_id)->method_documentation->{method_name};


Each of these calls returns a hashref with various useful pieces of information.

# LOAD THE MODULES

To load the API packages:
```perl
use WWW::SwaggerClient::AnotherFakeApi;
use WWW::SwaggerClient::FakeApi;
use WWW::SwaggerClient::FakeClassnameTags123Api;
use WWW::SwaggerClient::PetApi;
use WWW::SwaggerClient::StoreApi;
use WWW::SwaggerClient::UserApi;

```

To load the models:
```perl
use WWW::SwaggerClient::Object::AdditionalPropertiesClass;
use WWW::SwaggerClient::Object::Animal;
use WWW::SwaggerClient::Object::AnimalFarm;
use WWW::SwaggerClient::Object::ApiResponse;
use WWW::SwaggerClient::Object::ArrayOfArrayOfNumberOnly;
use WWW::SwaggerClient::Object::ArrayOfNumberOnly;
use WWW::SwaggerClient::Object::ArrayTest;
use WWW::SwaggerClient::Object::Capitalization;
use WWW::SwaggerClient::Object::Category;
use WWW::SwaggerClient::Object::ClassModel;
use WWW::SwaggerClient::Object::Client;
use WWW::SwaggerClient::Object::EnumArrays;
use WWW::SwaggerClient::Object::EnumClass;
use WWW::SwaggerClient::Object::EnumTest;
use WWW::SwaggerClient::Object::FormatTest;
use WWW::SwaggerClient::Object::HasOnlyReadOnly;
use WWW::SwaggerClient::Object::List;
use WWW::SwaggerClient::Object::MapTest;
use WWW::SwaggerClient::Object::MixedPropertiesAndAdditionalPropertiesClass;
use WWW::SwaggerClient::Object::Model200Response;
use WWW::SwaggerClient::Object::ModelReturn;
use WWW::SwaggerClient::Object::Name;
use WWW::SwaggerClient::Object::NumberOnly;
use WWW::SwaggerClient::Object::Order;
use WWW::SwaggerClient::Object::OuterBoolean;
use WWW::SwaggerClient::Object::OuterComposite;
use WWW::SwaggerClient::Object::OuterEnum;
use WWW::SwaggerClient::Object::OuterNumber;
use WWW::SwaggerClient::Object::OuterString;
use WWW::SwaggerClient::Object::Pet;
use WWW::SwaggerClient::Object::ReadOnlyFirst;
use WWW::SwaggerClient::Object::SpecialModelName;
use WWW::SwaggerClient::Object::Tag;
use WWW::SwaggerClient::Object::User;
use WWW::SwaggerClient::Object::Cat;
use WWW::SwaggerClient::Object::Dog;

````

# GETTING STARTED
Put the Perl SDK under the 'lib' folder in your project directory, then run the following
```perl
#!/usr/bin/perl
use lib 'lib';
use strict;
use warnings;
# load the API package
use WWW::SwaggerClient::AnotherFakeApi;
use WWW::SwaggerClient::FakeApi;
use WWW::SwaggerClient::FakeClassnameTags123Api;
use WWW::SwaggerClient::PetApi;
use WWW::SwaggerClient::StoreApi;
use WWW::SwaggerClient::UserApi;

# load the models
use WWW::SwaggerClient::Object::AdditionalPropertiesClass;
use WWW::SwaggerClient::Object::Animal;
use WWW::SwaggerClient::Object::AnimalFarm;
use WWW::SwaggerClient::Object::ApiResponse;
use WWW::SwaggerClient::Object::ArrayOfArrayOfNumberOnly;
use WWW::SwaggerClient::Object::ArrayOfNumberOnly;
use WWW::SwaggerClient::Object::ArrayTest;
use WWW::SwaggerClient::Object::Capitalization;
use WWW::SwaggerClient::Object::Category;
use WWW::SwaggerClient::Object::ClassModel;
use WWW::SwaggerClient::Object::Client;
use WWW::SwaggerClient::Object::EnumArrays;
use WWW::SwaggerClient::Object::EnumClass;
use WWW::SwaggerClient::Object::EnumTest;
use WWW::SwaggerClient::Object::FormatTest;
use WWW::SwaggerClient::Object::HasOnlyReadOnly;
use WWW::SwaggerClient::Object::List;
use WWW::SwaggerClient::Object::MapTest;
use WWW::SwaggerClient::Object::MixedPropertiesAndAdditionalPropertiesClass;
use WWW::SwaggerClient::Object::Model200Response;
use WWW::SwaggerClient::Object::ModelReturn;
use WWW::SwaggerClient::Object::Name;
use WWW::SwaggerClient::Object::NumberOnly;
use WWW::SwaggerClient::Object::Order;
use WWW::SwaggerClient::Object::OuterBoolean;
use WWW::SwaggerClient::Object::OuterComposite;
use WWW::SwaggerClient::Object::OuterEnum;
use WWW::SwaggerClient::Object::OuterNumber;
use WWW::SwaggerClient::Object::OuterString;
use WWW::SwaggerClient::Object::Pet;
use WWW::SwaggerClient::Object::ReadOnlyFirst;
use WWW::SwaggerClient::Object::SpecialModelName;
use WWW::SwaggerClient::Object::Tag;
use WWW::SwaggerClient::Object::User;
use WWW::SwaggerClient::Object::Cat;
use WWW::SwaggerClient::Object::Dog;

# for displaying the API response data
use Data::Dumper;
use WWW::SwaggerClient::;

my $api_instance = WWW::SwaggerClient::->new(
);

my $body = WWW::SwaggerClient::Object::Client->new(); # Client | client model

eval {
    my $result = $api_instance->test_special_tags(body => $body);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling AnotherFakeApi->test_special_tags: $@\n";
}

```

# DOCUMENTATION FOR API ENDPOINTS

All URIs are relative to *http://petstore.swagger.io:80/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnotherFakeApi* | [**test_special_tags**](docs/AnotherFakeApi.md#test_special_tags) | **PATCH** /another-fake/dummy | To test special tags
*FakeApi* | [**fake_outer_boolean_serialize**](docs/FakeApi.md#fake_outer_boolean_serialize) | **POST** /fake/outer/boolean | 
*FakeApi* | [**fake_outer_composite_serialize**](docs/FakeApi.md#fake_outer_composite_serialize) | **POST** /fake/outer/composite | 
*FakeApi* | [**fake_outer_number_serialize**](docs/FakeApi.md#fake_outer_number_serialize) | **POST** /fake/outer/number | 
*FakeApi* | [**fake_outer_string_serialize**](docs/FakeApi.md#fake_outer_string_serialize) | **POST** /fake/outer/string | 
*FakeApi* | [**test_body_with_query_params**](docs/FakeApi.md#test_body_with_query_params) | **PUT** /fake/body-with-query-params | 
*FakeApi* | [**test_client_model**](docs/FakeApi.md#test_client_model) | **PATCH** /fake | To test \&quot;client\&quot; model
*FakeApi* | [**test_endpoint_parameters**](docs/FakeApi.md#test_endpoint_parameters) | **POST** /fake | Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
*FakeApi* | [**test_enum_parameters**](docs/FakeApi.md#test_enum_parameters) | **GET** /fake | To test enum parameters
*FakeApi* | [**test_inline_additional_properties**](docs/FakeApi.md#test_inline_additional_properties) | **POST** /fake/inline-additionalProperties | test inline additionalProperties
*FakeApi* | [**test_json_form_data**](docs/FakeApi.md#test_json_form_data) | **GET** /fake/jsonFormData | test json serialization of form data
*FakeClassnameTags123Api* | [**test_classname**](docs/FakeClassnameTags123Api.md#test_classname) | **PATCH** /fake_classname_test | To test class name in snake case
*PetApi* | [**add_pet**](docs/PetApi.md#add_pet) | **POST** /pet | Add a new pet to the store
*PetApi* | [**delete_pet**](docs/PetApi.md#delete_pet) | **DELETE** /pet/{petId} | Deletes a pet
*PetApi* | [**find_pets_by_status**](docs/PetApi.md#find_pets_by_status) | **GET** /pet/findByStatus | Finds Pets by status
*PetApi* | [**find_pets_by_tags**](docs/PetApi.md#find_pets_by_tags) | **GET** /pet/findByTags | Finds Pets by tags
*PetApi* | [**get_pet_by_id**](docs/PetApi.md#get_pet_by_id) | **GET** /pet/{petId} | Find pet by ID
*PetApi* | [**update_pet**](docs/PetApi.md#update_pet) | **PUT** /pet | Update an existing pet
*PetApi* | [**update_pet_with_form**](docs/PetApi.md#update_pet_with_form) | **POST** /pet/{petId} | Updates a pet in the store with form data
*PetApi* | [**upload_file**](docs/PetApi.md#upload_file) | **POST** /pet/{petId}/uploadImage | uploads an image
*StoreApi* | [**delete_order**](docs/StoreApi.md#delete_order) | **DELETE** /store/order/{order_id} | Delete purchase order by ID
*StoreApi* | [**get_inventory**](docs/StoreApi.md#get_inventory) | **GET** /store/inventory | Returns pet inventories by status
*StoreApi* | [**get_order_by_id**](docs/StoreApi.md#get_order_by_id) | **GET** /store/order/{order_id} | Find purchase order by ID
*StoreApi* | [**place_order**](docs/StoreApi.md#place_order) | **POST** /store/order | Place an order for a pet
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create user
*UserApi* | [**create_users_with_array_input**](docs/UserApi.md#create_users_with_array_input) | **POST** /user/createWithArray | Creates list of users with given input array
*UserApi* | [**create_users_with_list_input**](docs/UserApi.md#create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **GET** /user/login | Logs user into the system
*UserApi* | [**logout_user**](docs/UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{username} | Updated user


# DOCUMENTATION FOR MODELS
 - [WWW::SwaggerClient::Object::AdditionalPropertiesClass](docs/AdditionalPropertiesClass.md)
 - [WWW::SwaggerClient::Object::Animal](docs/Animal.md)
 - [WWW::SwaggerClient::Object::AnimalFarm](docs/AnimalFarm.md)
 - [WWW::SwaggerClient::Object::ApiResponse](docs/ApiResponse.md)
 - [WWW::SwaggerClient::Object::ArrayOfArrayOfNumberOnly](docs/ArrayOfArrayOfNumberOnly.md)
 - [WWW::SwaggerClient::Object::ArrayOfNumberOnly](docs/ArrayOfNumberOnly.md)
 - [WWW::SwaggerClient::Object::ArrayTest](docs/ArrayTest.md)
 - [WWW::SwaggerClient::Object::Capitalization](docs/Capitalization.md)
 - [WWW::SwaggerClient::Object::Category](docs/Category.md)
 - [WWW::SwaggerClient::Object::ClassModel](docs/ClassModel.md)
 - [WWW::SwaggerClient::Object::Client](docs/Client.md)
 - [WWW::SwaggerClient::Object::EnumArrays](docs/EnumArrays.md)
 - [WWW::SwaggerClient::Object::EnumClass](docs/EnumClass.md)
 - [WWW::SwaggerClient::Object::EnumTest](docs/EnumTest.md)
 - [WWW::SwaggerClient::Object::FormatTest](docs/FormatTest.md)
 - [WWW::SwaggerClient::Object::HasOnlyReadOnly](docs/HasOnlyReadOnly.md)
 - [WWW::SwaggerClient::Object::List](docs/List.md)
 - [WWW::SwaggerClient::Object::MapTest](docs/MapTest.md)
 - [WWW::SwaggerClient::Object::MixedPropertiesAndAdditionalPropertiesClass](docs/MixedPropertiesAndAdditionalPropertiesClass.md)
 - [WWW::SwaggerClient::Object::Model200Response](docs/Model200Response.md)
 - [WWW::SwaggerClient::Object::ModelReturn](docs/ModelReturn.md)
 - [WWW::SwaggerClient::Object::Name](docs/Name.md)
 - [WWW::SwaggerClient::Object::NumberOnly](docs/NumberOnly.md)
 - [WWW::SwaggerClient::Object::Order](docs/Order.md)
 - [WWW::SwaggerClient::Object::OuterBoolean](docs/OuterBoolean.md)
 - [WWW::SwaggerClient::Object::OuterComposite](docs/OuterComposite.md)
 - [WWW::SwaggerClient::Object::OuterEnum](docs/OuterEnum.md)
 - [WWW::SwaggerClient::Object::OuterNumber](docs/OuterNumber.md)
 - [WWW::SwaggerClient::Object::OuterString](docs/OuterString.md)
 - [WWW::SwaggerClient::Object::Pet](docs/Pet.md)
 - [WWW::SwaggerClient::Object::ReadOnlyFirst](docs/ReadOnlyFirst.md)
 - [WWW::SwaggerClient::Object::SpecialModelName](docs/SpecialModelName.md)
 - [WWW::SwaggerClient::Object::Tag](docs/Tag.md)
 - [WWW::SwaggerClient::Object::User](docs/User.md)
 - [WWW::SwaggerClient::Object::Cat](docs/Cat.md)
 - [WWW::SwaggerClient::Object::Dog](docs/Dog.md)


# DOCUMENTATION FOR AUTHORIZATION

## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## api_key_query

- **Type**: API key
- **API key parameter name**: api_key_query
- **Location**: URL query string

## http_basic_test

- **Type**: HTTP basic authentication

## petstore_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: http://petstore.swagger.io/api/oauth/dialog
- **Scopes**: 
  - **write:pets**: modify pets in your account
  - **read:pets**: read your pets
