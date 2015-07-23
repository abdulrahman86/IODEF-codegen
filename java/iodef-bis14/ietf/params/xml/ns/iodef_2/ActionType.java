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
 * <p>Java class for action-type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="action-type"&gt;
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}NMTOKEN"&gt;
 *     &lt;enumeration value="nothing"/&gt;
 *     &lt;enumeration value="contact-source-site"/&gt;
 *     &lt;enumeration value="contact-target-site"/&gt;
 *     &lt;enumeration value="contact-sender"/&gt;
 *     &lt;enumeration value="investigate"/&gt;
 *     &lt;enumeration value="block-host"/&gt;
 *     &lt;enumeration value="block-network"/&gt;
 *     &lt;enumeration value="block-port"/&gt;
 *     &lt;enumeration value="rate-limit-host"/&gt;
 *     &lt;enumeration value="rate-limit-network"/&gt;
 *     &lt;enumeration value="rate-limit-port"/&gt;
 *     &lt;enumeration value="redirect-traffic"/&gt;
 *     &lt;enumeration value="honeypot"/&gt;
 *     &lt;enumeration value="upgrade-software"/&gt;
 *     &lt;enumeration value="rebuild-asset"/&gt;
 *     &lt;enumeration value="harden-asset"/&gt;
 *     &lt;enumeration value="remediate-other"/&gt;
 *     &lt;enumeration value="status-triage"/&gt;
 *     &lt;enumeration value="status-new-info"/&gt;
 *     &lt;enumeration value="watch-and-report"/&gt;
 *     &lt;enumeration value="defined-coa"/&gt;
 *     &lt;enumeration value="other"/&gt;
 *     &lt;enumeration value="ext-value"/&gt;
 *   &lt;/restriction&gt;
 * &lt;/simpleType&gt;
 * </pre>
 * 
 */
@XmlType(name = "action-type")
@XmlEnum
public enum ActionType {

    @XmlEnumValue("nothing")
    NOTHING("nothing"),
    @XmlEnumValue("contact-source-site")
    CONTACT_SOURCE_SITE("contact-source-site"),
    @XmlEnumValue("contact-target-site")
    CONTACT_TARGET_SITE("contact-target-site"),
    @XmlEnumValue("contact-sender")
    CONTACT_SENDER("contact-sender"),
    @XmlEnumValue("investigate")
    INVESTIGATE("investigate"),
    @XmlEnumValue("block-host")
    BLOCK_HOST("block-host"),
    @XmlEnumValue("block-network")
    BLOCK_NETWORK("block-network"),
    @XmlEnumValue("block-port")
    BLOCK_PORT("block-port"),
    @XmlEnumValue("rate-limit-host")
    RATE_LIMIT_HOST("rate-limit-host"),
    @XmlEnumValue("rate-limit-network")
    RATE_LIMIT_NETWORK("rate-limit-network"),
    @XmlEnumValue("rate-limit-port")
    RATE_LIMIT_PORT("rate-limit-port"),
    @XmlEnumValue("redirect-traffic")
    REDIRECT_TRAFFIC("redirect-traffic"),
    @XmlEnumValue("honeypot")
    HONEYPOT("honeypot"),
    @XmlEnumValue("upgrade-software")
    UPGRADE_SOFTWARE("upgrade-software"),
    @XmlEnumValue("rebuild-asset")
    REBUILD_ASSET("rebuild-asset"),
    @XmlEnumValue("harden-asset")
    HARDEN_ASSET("harden-asset"),
    @XmlEnumValue("remediate-other")
    REMEDIATE_OTHER("remediate-other"),
    @XmlEnumValue("status-triage")
    STATUS_TRIAGE("status-triage"),
    @XmlEnumValue("status-new-info")
    STATUS_NEW_INFO("status-new-info"),
    @XmlEnumValue("watch-and-report")
    WATCH_AND_REPORT("watch-and-report"),
    @XmlEnumValue("defined-coa")
    DEFINED_COA("defined-coa"),
    @XmlEnumValue("other")
    OTHER("other"),
    @XmlEnumValue("ext-value")
    EXT_VALUE("ext-value");
    private final String value;

    ActionType(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static ActionType fromValue(String v) {
        for (ActionType c: ActionType.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}