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
 * <p>Java class for duration-type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="duration-type"&gt;
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}NMTOKEN"&gt;
 *     &lt;enumeration value="second"/&gt;
 *     &lt;enumeration value="minute"/&gt;
 *     &lt;enumeration value="hour"/&gt;
 *     &lt;enumeration value="day"/&gt;
 *     &lt;enumeration value="month"/&gt;
 *     &lt;enumeration value="quarter"/&gt;
 *     &lt;enumeration value="year"/&gt;
 *     &lt;enumeration value="ext-value"/&gt;
 *   &lt;/restriction&gt;
 * &lt;/simpleType&gt;
 * </pre>
 * 
 */
@XmlType(name = "duration-type")
@XmlEnum
public enum DurationType {

    @XmlEnumValue("second")
    SECOND("second"),
    @XmlEnumValue("minute")
    MINUTE("minute"),
    @XmlEnumValue("hour")
    HOUR("hour"),
    @XmlEnumValue("day")
    DAY("day"),
    @XmlEnumValue("month")
    MONTH("month"),
    @XmlEnumValue("quarter")
    QUARTER("quarter"),
    @XmlEnumValue("year")
    YEAR("year"),
    @XmlEnumValue("ext-value")
    EXT_VALUE("ext-value");
    private final String value;

    DurationType(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static DurationType fromValue(String v) {
        for (DurationType c: DurationType.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}