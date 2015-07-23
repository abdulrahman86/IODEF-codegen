//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.11 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2015.07.23 at 09:39:40 PM JST 
//


package ietf.params.xml.ns.iodef_2;

import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for proto-dtype-type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="proto-dtype-type"&gt;
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}NMTOKEN"&gt;
 *     &lt;enumeration value="boolean"/&gt;
 *     &lt;enumeration value="byte"/&gt;
 *     &lt;enumeration value="bytes"/&gt;
 *     &lt;enumeration value="character"/&gt;
 *     &lt;enumeration value="date-time"/&gt;
 *     &lt;enumeration value="integer"/&gt;
 *     &lt;enumeration value="real"/&gt;
 *     &lt;enumeration value="string"/&gt;
 *     &lt;enumeration value="xml"/&gt;
 *     &lt;enumeration value="ext-value"/&gt;
 *   &lt;/restriction&gt;
 * &lt;/simpleType&gt;
 * </pre>
 * 
 */
@XmlType(name = "proto-dtype-type")
@XmlEnum
public enum ProtoDtypeType {

    @XmlEnumValue("boolean")
    BOOLEAN("boolean"),
    @XmlEnumValue("byte")
    BYTE("byte"),
    @XmlEnumValue("bytes")
    BYTES("bytes"),
    @XmlEnumValue("character")
    CHARACTER("character"),
    @XmlEnumValue("date-time")
    DATE_TIME("date-time"),
    @XmlEnumValue("integer")
    INTEGER("integer"),
    @XmlEnumValue("real")
    REAL("real"),
    @XmlEnumValue("string")
    STRING("string"),
    @XmlEnumValue("xml")
    XML("xml"),
    @XmlEnumValue("ext-value")
    EXT_VALUE("ext-value");
    private final String value;

    ProtoDtypeType(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static ProtoDtypeType fromValue(String v) {
        for (ProtoDtypeType c: ProtoDtypeType.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}