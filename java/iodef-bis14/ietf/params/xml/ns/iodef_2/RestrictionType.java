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
 * <p>Java class for restriction-type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="restriction-type"&gt;
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}NMTOKEN"&gt;
 *     &lt;enumeration value="default"/&gt;
 *     &lt;enumeration value="public"/&gt;
 *     &lt;enumeration value="partner"/&gt;
 *     &lt;enumeration value="need-to-know"/&gt;
 *     &lt;enumeration value="private"/&gt;
 *     &lt;enumeration value="white"/&gt;
 *     &lt;enumeration value="green"/&gt;
 *     &lt;enumeration value="amber"/&gt;
 *     &lt;enumeration value="red"/&gt;
 *     &lt;enumeration value="ext-value"/&gt;
 *   &lt;/restriction&gt;
 * &lt;/simpleType&gt;
 * </pre>
 * 
 */
@XmlType(name = "restriction-type")
@XmlEnum
public enum RestrictionType {

    @XmlEnumValue("default")
    DEFAULT("default"),
    @XmlEnumValue("public")
    PUBLIC("public"),
    @XmlEnumValue("partner")
    PARTNER("partner"),
    @XmlEnumValue("need-to-know")
    NEED_TO_KNOW("need-to-know"),
    @XmlEnumValue("private")
    PRIVATE("private"),
    @XmlEnumValue("white")
    WHITE("white"),
    @XmlEnumValue("green")
    GREEN("green"),
    @XmlEnumValue("amber")
    AMBER("amber"),
    @XmlEnumValue("red")
    RED("red"),
    @XmlEnumValue("ext-value")
    EXT_VALUE("ext-value");
    private final String value;

    RestrictionType(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static RestrictionType fromValue(String v) {
        for (RestrictionType c: RestrictionType.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}