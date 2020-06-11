<?php
/**
 * Invoice
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
 * Invoice Class Doc Comment
 *
 * @category Class
 * @description The shipment invoice required for commercial shipment.
 * @package  PurplShip
 * @author   PurplShip Codegen team
 * @link     https://github.com/purplship/purplship-clients
 */
class Invoice implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'Invoice';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'date' => 'string',
        'identifier' => 'string',
        'type' => 'string',
        'copies' => 'int'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'date' => null,
        'identifier' => null,
        'type' => null,
        'copies' => null
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
        'date' => 'date',
        'identifier' => 'identifier',
        'type' => 'type',
        'copies' => 'copies'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'date' => 'setDate',
        'identifier' => 'setIdentifier',
        'type' => 'setType',
        'copies' => 'setCopies'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'date' => 'getDate',
        'identifier' => 'getIdentifier',
        'type' => 'getType',
        'copies' => 'getCopies'
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
        $this->container['date'] = isset($data['date']) ? $data['date'] : null;
        $this->container['identifier'] = isset($data['identifier']) ? $data['identifier'] : null;
        $this->container['type'] = isset($data['type']) ? $data['type'] : null;
        $this->container['copies'] = isset($data['copies']) ? $data['copies'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['date'] === null) {
            $invalidProperties[] = "'date' can't be null";
        }
        if ((mb_strlen($this->container['date']) < 1)) {
            $invalidProperties[] = "invalid value for 'date', the character length must be bigger than or equal to 1.";
        }

        if (!is_null($this->container['identifier']) && (mb_strlen($this->container['identifier']) < 1)) {
            $invalidProperties[] = "invalid value for 'identifier', the character length must be bigger than or equal to 1.";
        }

        if (!is_null($this->container['type']) && (mb_strlen($this->container['type']) < 1)) {
            $invalidProperties[] = "invalid value for 'type', the character length must be bigger than or equal to 1.";
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
     * Gets date
     *
     * @return string
     */
    public function getDate()
    {
        return $this->container['date'];
    }

    /**
     * Sets date
     *
     * @param string $date The invoice date
     *
     * @return $this
     */
    public function setDate($date)
    {

        if ((mb_strlen($date) < 1)) {
            throw new \InvalidArgumentException('invalid length for $date when calling Invoice., must be bigger than or equal to 1.');
        }

        $this->container['date'] = $date;

        return $this;
    }

    /**
     * Gets identifier
     *
     * @return string
     */
    public function getIdentifier()
    {
        return $this->container['identifier'];
    }

    /**
     * Sets identifier
     *
     * @param string $identifier The internal invoice document identifier
     *
     * @return $this
     */
    public function setIdentifier($identifier)
    {

        if (!is_null($identifier) && (mb_strlen($identifier) < 1)) {
            throw new \InvalidArgumentException('invalid length for $identifier when calling Invoice., must be bigger than or equal to 1.');
        }

        $this->container['identifier'] = $identifier;

        return $this;
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
     * @param string $type The invoice type
     *
     * @return $this
     */
    public function setType($type)
    {

        if (!is_null($type) && (mb_strlen($type) < 1)) {
            throw new \InvalidArgumentException('invalid length for $type when calling Invoice., must be bigger than or equal to 1.');
        }

        $this->container['type'] = $type;

        return $this;
    }

    /**
     * Gets copies
     *
     * @return int
     */
    public function getCopies()
    {
        return $this->container['copies'];
    }

    /**
     * Sets copies
     *
     * @param int $copies The number of invoice copies
     *
     * @return $this
     */
    public function setCopies($copies)
    {
        $this->container['copies'] = $copies;

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


