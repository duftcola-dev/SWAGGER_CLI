<?php

/**
 * StoreController
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Server\Controller
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * Swagger Petstore
 *
 * This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * OpenAPI spec version: 1.0.0
 * Contact: apiteam@swagger.io
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 *
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Server\Controller;

use \Exception;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Exception\HttpException;
use Symfony\Component\Validator\Constraints as Assert;
use Swagger\Server\Api\StoreApiInterface;
use Swagger\Server\Model\Order;

/**
 * StoreController Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Server\Controller
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class StoreController extends Controller
{

    /**
     * Operation deleteOrder
     *
     * Delete purchase order by ID
     *
     * @param Request $request The Symfony request to handle.
     * @return Response The Symfony response.
     */
    public function deleteOrderAction(Request $request, $orderId)
    {
        // Figure out what data format to return to the client
        $produces = ['application/xml', 'application/json'];
        // Figure out what the client accepts
        $clientAccepts = $request->headers->has('Accept')?$request->headers->get('Accept'):'*/*';
        $responseFormat = $this->getOutputFormat($clientAccepts, $produces);
        if ($responseFormat === null) {
            return new Response('', 406);
        }

        // Handle authentication

        // Read out all input parameter values into variables

        // Use the default value if no value was provided

        // Deserialize the input values that needs it
        $orderId = $this->deserialize($orderId, 'string', 'string');

        // Validate the input values
        $asserts = [];
        $asserts[] = new Assert\NotNull();
        $asserts[] = new Assert\Type("string");
        $response = $this->validate($orderId, $asserts);
        if ($response instanceof Response) {
            return $response;
        }


        try {
            $handler = $this->getApiHandler();

            
            // Make the call to the business logic
            $responseCode = 204;
            $responseHeaders = [];
            $result = $handler->deleteOrder($orderId, $responseCode, $responseHeaders);

            // Find default response message
            $message = '';

            // Find a more specific message, if available
            switch ($responseCode) {
                case 400:
                    $message = 'Invalid ID supplied';
                    break;
                case 404:
                    $message = 'Order not found';
                    break;
            }

            return new Response(
                $result?$this->serialize($result, $responseFormat):'',
                $responseCode,
                array_merge(
                    $responseHeaders,
                    [
                        'Content-Type' => $responseFormat,
                        'X-Swagger-Message' => $message
                    ]
                )
            );
        } catch (Exception $fallthrough) {
            return $this->createErrorResponse(new HttpException(500, 'An unsuspected error occurred.', $fallthrough));
        }
    }

    /**
     * Operation getInventory
     *
     * Returns pet inventories by status
     *
     * @param Request $request The Symfony request to handle.
     * @return Response The Symfony response.
     */
    public function getInventoryAction(Request $request)
    {
        // Figure out what data format to return to the client
        $produces = ['application/json'];
        // Figure out what the client accepts
        $clientAccepts = $request->headers->has('Accept')?$request->headers->get('Accept'):'*/*';
        $responseFormat = $this->getOutputFormat($clientAccepts, $produces);
        if ($responseFormat === null) {
            return new Response('', 406);
        }

        // Handle authentication
        // Authentication 'api_key' required
        // Set key with prefix in header
        $securityapi_key = $request->headers->get('api_key');

        // Read out all input parameter values into variables

        // Use the default value if no value was provided

        // Deserialize the input values that needs it

        // Validate the input values


        try {
            $handler = $this->getApiHandler();

            // Set authentication method 'api_key'
            $handler->setapi_key($securityapi_key);
            
            // Make the call to the business logic
            $responseCode = 200;
            $responseHeaders = [];
            $result = $handler->getInventory($responseCode, $responseHeaders);

            // Find default response message
            $message = 'successful operation';

            // Find a more specific message, if available
            switch ($responseCode) {
                case 200:
                    $message = 'successful operation';
                    break;
            }

            return new Response(
                $result?$this->serialize($result, $responseFormat):'',
                $responseCode,
                array_merge(
                    $responseHeaders,
                    [
                        'Content-Type' => $responseFormat,
                        'X-Swagger-Message' => $message
                    ]
                )
            );
        } catch (Exception $fallthrough) {
            return $this->createErrorResponse(new HttpException(500, 'An unsuspected error occurred.', $fallthrough));
        }
    }

    /**
     * Operation getOrderById
     *
     * Find purchase order by ID
     *
     * @param Request $request The Symfony request to handle.
     * @return Response The Symfony response.
     */
    public function getOrderByIdAction(Request $request, $orderId)
    {
        // Figure out what data format to return to the client
        $produces = ['application/xml', 'application/json'];
        // Figure out what the client accepts
        $clientAccepts = $request->headers->has('Accept')?$request->headers->get('Accept'):'*/*';
        $responseFormat = $this->getOutputFormat($clientAccepts, $produces);
        if ($responseFormat === null) {
            return new Response('', 406);
        }

        // Handle authentication

        // Read out all input parameter values into variables

        // Use the default value if no value was provided

        // Deserialize the input values that needs it
        $orderId = $this->deserialize($orderId, 'int', 'string');

        // Validate the input values
        $asserts = [];
        $asserts[] = new Assert\NotNull();
        $asserts[] = new Assert\Type("int");
        $asserts[] = new Assert\GreaterThanOrEqual(1);
        $asserts[] = new Assert\LessThanOrEqual(5);
        $response = $this->validate($orderId, $asserts);
        if ($response instanceof Response) {
            return $response;
        }


        try {
            $handler = $this->getApiHandler();

            
            // Make the call to the business logic
            $responseCode = 200;
            $responseHeaders = [];
            $result = $handler->getOrderById($orderId, $responseCode, $responseHeaders);

            // Find default response message
            $message = 'successful operation';

            // Find a more specific message, if available
            switch ($responseCode) {
                case 200:
                    $message = 'successful operation';
                    break;
                case 400:
                    $message = 'Invalid ID supplied';
                    break;
                case 404:
                    $message = 'Order not found';
                    break;
            }

            return new Response(
                $result?$this->serialize($result, $responseFormat):'',
                $responseCode,
                array_merge(
                    $responseHeaders,
                    [
                        'Content-Type' => $responseFormat,
                        'X-Swagger-Message' => $message
                    ]
                )
            );
        } catch (Exception $fallthrough) {
            return $this->createErrorResponse(new HttpException(500, 'An unsuspected error occurred.', $fallthrough));
        }
    }

    /**
     * Operation placeOrder
     *
     * Place an order for a pet
     *
     * @param Request $request The Symfony request to handle.
     * @return Response The Symfony response.
     */
    public function placeOrderAction(Request $request)
    {
        // Make sure that the client is providing something that we can consume
        $consumes = [];
        $inputFormat = $request->headers->has('Content-Type')?$request->headers->get('Content-Type'):$consumes[0];
        if (!in_array($inputFormat, $consumes)) {
            // We can't consume the content that the client is sending us
            return new Response('', 415);
        }

        // Figure out what data format to return to the client
        $produces = ['application/xml', 'application/json'];
        // Figure out what the client accepts
        $clientAccepts = $request->headers->has('Accept')?$request->headers->get('Accept'):'*/*';
        $responseFormat = $this->getOutputFormat($clientAccepts, $produces);
        if ($responseFormat === null) {
            return new Response('', 406);
        }

        // Handle authentication

        // Read out all input parameter values into variables
        $body = $request->getContent();

        // Use the default value if no value was provided

        // Deserialize the input values that needs it
        $body = $this->deserialize($body, 'Swagger\Server\Model\Order', $inputFormat);

        // Validate the input values
        $asserts = [];
        $asserts[] = new Assert\NotNull();
        $asserts[] = new Assert\Type("Swagger\Server\Model\Order");
        $response = $this->validate($body, $asserts);
        if ($response instanceof Response) {
            return $response;
        }


        try {
            $handler = $this->getApiHandler();

            
            // Make the call to the business logic
            $responseCode = 200;
            $responseHeaders = [];
            $result = $handler->placeOrder($body, $responseCode, $responseHeaders);

            // Find default response message
            $message = 'successful operation';

            // Find a more specific message, if available
            switch ($responseCode) {
                case 200:
                    $message = 'successful operation';
                    break;
                case 400:
                    $message = 'Invalid Order';
                    break;
            }

            return new Response(
                $result?$this->serialize($result, $responseFormat):'',
                $responseCode,
                array_merge(
                    $responseHeaders,
                    [
                        'Content-Type' => $responseFormat,
                        'X-Swagger-Message' => $message
                    ]
                )
            );
        } catch (Exception $fallthrough) {
            return $this->createErrorResponse(new HttpException(500, 'An unsuspected error occurred.', $fallthrough));
        }
    }

    /**
     * Returns the handler for this API controller.
     * @return StoreApiInterface
     */
    public function getApiHandler()
    {
        return $this->apiServer->getApiHandler('store');
    }
}
