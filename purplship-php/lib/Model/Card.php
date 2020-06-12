<?php
/**
 * Card
 *
 * PHP version 5
 *
 * @category Class
 * @package  PurplShip
 * @author   PurplShip Codegen team
 * @link     https://github.com/purplship/purplship-clients
 */

/**
 * PurplShip Multi-carrier API
 *
 * PurplShip is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services
 *
 * OpenAPI spec version: v1
 * Contact: hello@purplship.com
 * Generated by: https://github.com/purplship/purplship-clients.git
 * PurplShip Codegen version: 2.4.14
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/purplship/purplship-clients
 * Do not edit the class manually.
 */

namespace PurplShip\Model;

use \ArrayAccess;
use \PurplShip\ObjectSerializer;

/**
 * Card Class Doc Comment
 *
 * @category Class
 * @description The payment credit card for payment by card
 * @package  PurplShip
 * @author   PurplShip Codegen team
 * @link     https://github.com/purplship/purplship-clients
 */
class Card implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'Card';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'type' => 'string',
        'number' => 'string',
        'expiry_month' => 'string',
        'expiry_year' => 'string',
        'security_code' => 'string',
        'name' => 'string',
        'postal_code' => 'string'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'type' => null,
        'number' => null,
        'expiry_month' => null,
        'expiry_year' => null,
        'security_code' => null,
        'name' => null,
        'postal_code' => null
    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'type' => 'type',
        'number' => 'number',
        'expiry_month' => 'expiryMonth',
        'expiry_year' => 'expiryYear',
        'security_code' => 'securityCode',
        'name' => 'name',
        'postal_code' => 'postalCode'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'type' => 'setType',
        'number' => 'setNumber',
        'expiry_month' => 'setExpiryMonth',
        'expiry_year' => 'setExpiryYear',
        'security_code' => 'setSecurityCode',
        'name' => 'setName',
        'postal_code' => 'setPostalCode'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'type' => 'getType',
        'number' => 'getNumber',
        'expiry_month' => 'getExpiryMonth',
        'expiry_year' => 'getExpiryYear',
        'security_code' => 'getSecurityCode',
        'name' => 'getName',
        'postal_code' => 'getPostalCode'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['type'] = isset($data['type']) ? $data['type'] : null;
        $this->container['number'] = isset($data['number']) ? $data['number'] : null;
        $this->container['expiry_month'] = isset($data['expiry_month']) ? $data['expiry_month'] : null;
        $this->container['expiry_year'] = isset($data['expiry_year']) ? $data['expiry_year'] : null;
        $this->container['security_code'] = isset($data['security_code']) ? $data['security_code'] : null;
        $this->container['name'] = isset($data['name']) ? $data['name'] : null;
        $this->container['postal_code'] = isset($data['postal_code']) ? $data['postal_code'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['type'] === null) {
            $invalidProperties[] = "'type' can't be null";
        }
        if ((mb_strlen($this->container['type']) < 1)) {
            $invalidProperties[] = "invalid value for 'type', the character length must be bigger than or equal to 1.";
        }

        if ($this->container['number'] === null) {
            $invalidProperties[] = "'number' can't be null";
        }
        if ((mb_strlen($this->container['number']) < 1)) {
            $invalidProperties[] = "invalid value for 'number', the character length must be bigger than or equal to 1.";
        }

        if ($this->container['expiry_month'] === null) {
            $invalidProperties[] = "'expiry_month' can't be null";
        }
        if ((mb_strlen($this->container['expiry_month']) < 1)) {
            $invalidProperties[] = "invalid value for 'expiry_month', the character length must be bigger than or equal to 1.";
        }

        if ($this->container['expiry_year'] === null) {
            $invalidProperties[] = "'expiry_year' can't be null";
        }
        if ((mb_strlen($this->container['expiry_year']) < 1)) {
            $invalidProperties[] = "invalid value for 'expiry_year', the character length must be bigger than or equal to 1.";
        }

        if ($this->container['security_code'] === null) {
            $invalidProperties[] = "'security_code' can't be null";
        }
        if ((mb_strlen($this->container['security_code']) < 1)) {
            $invalidProperties[] = "invalid value for 'security_code', the character length must be bigger than or equal to 1.";
        }

        if (!is_null($this->container['name']) && (mb_strlen($this->container['name']) < 1)) {
            $invalidProperties[] = "invalid value for 'name', the character length must be bigger than or equal to 1.";
        }

        if (!is_null($this->container['postal_code']) && (mb_strlen($this->container['postal_code']) < 1)) {
            $invalidProperties[] = "invalid value for 'postal_code', the character length must be bigger than or equal to 1.";
        }

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets type
     *
     * @return string
     */
    public function getType()
    {
        return $this->container['type'];
    }

    /**
     * Sets type
     *
     * @param string $type The credit card type
     *
     * @return $this
     */
    public function setType($type)
    {

        if ((mb_strlen($type) < 1)) {
            throw new \InvalidArgumentException('invalid length for $type when calling Card., must be bigger than or equal to 1.');
        }

        $this->container['type'] = $type;

        return $this;
    }

    /**
     * Gets number
     *
     * @return string
     */
    public function getNumber()
    {
        return $this->container['number'];
    }

    /**
     * Sets number
     *
     * @param string $number The credit card number
     *
     * @return $this
     */
    public function setNumber($number)
    {

        if ((mb_strlen($number) < 1)) {
            throw new \InvalidArgumentException('invalid length for $number when calling Card., must be bigger than or equal to 1.');
        }

        $this->container['number'] = $number;

        return $this;
    }

    /**
     * Gets expiry_month
     *
     * @return string
     */
    public function getExpiryMonth()
    {
        return $this->container['expiry_month'];
    }

    /**
     * Sets expiry_month
     *
     * @param string $expiry_month The credit card expiry month (MM)
     *
     * @return $this
     */
    public function setExpiryMonth($expiry_month)
    {

        if ((mb_strlen($expiry_month) < 1)) {
            throw new \InvalidArgumentException('invalid length for $expiry_month when calling Card., must be bigger than or equal to 1.');
        }

        $this->container['expiry_month'] = $expiry_month;

        return $this;
    }

    /**
     * Gets expiry_year
     *
     * @return string
     */
    public function getExpiryYear()
    {
        return $this->container['expiry_year'];
    }

    /**
     * Sets expiry_year
     *
     * @param string $expiry_year The credit card expiry year (YYYY)
     *
     * @return $this
     */
    public function setExpiryYear($expiry_year)
    {

        if ((mb_strlen($expiry_year) < 1)) {
            throw new \InvalidArgumentException('invalid length for $expiry_year when calling Card., must be bigger than or equal to 1.');
        }

        $this->container['expiry_year'] = $expiry_year;

        return $this;
    }

    /**
     * Gets security_code
     *
     * @return string
     */
    public function getSecurityCode()
    {
        return $this->container['security_code'];
    }

    /**
     * Sets security_code
     *
     * @param string $security_code The credit card security code often at the back (000)
     *
     * @return $this
     */
    public function setSecurityCode($security_code)
    {

        if ((mb_strlen($security_code) < 1)) {
            throw new \InvalidArgumentException('invalid length for $security_code when calling Card., must be bigger than or equal to 1.');
        }

        $this->container['security_code'] = $security_code;

        return $this;
    }

    /**
     * Gets name
     *
     * @return string
     */
    public function getName()
    {
        return $this->container['name'];
    }

    /**
     * Sets name
     *
     * @param string $name The name inscribed on the credit card
     *
     * @return $this
     */
    public function setName($name)
    {

        if (!is_null($name) && (mb_strlen($name) < 1)) {
            throw new \InvalidArgumentException('invalid length for $name when calling Card., must be bigger than or equal to 1.');
        }

        $this->container['name'] = $name;

        return $this;
    }

    /**
     * Gets postal_code
     *
     * @return string
     */
    public function getPostalCode()
    {
        return $this->container['postal_code'];
    }

    /**
     * Sets postal_code
     *
     * @param string $postal_code The credit card registration address postal code
     *
     * @return $this
     */
    public function setPostalCode($postal_code)
    {

        if (!is_null($postal_code) && (mb_strlen($postal_code) < 1)) {
            throw new \InvalidArgumentException('invalid length for $postal_code when calling Card., must be bigger than or equal to 1.');
        }

        $this->container['postal_code'] = $postal_code;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


