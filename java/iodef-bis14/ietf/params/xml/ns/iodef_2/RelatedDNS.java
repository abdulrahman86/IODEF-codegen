//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.11 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2015.07.23 at 09:39:40 PM JST 
//


package ietf.params.xml.ns.iodef_2;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.XmlValue;
import javax.xml.bind.annotation.adapters.CollapsedStringAdapter;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType&gt;
 *   &lt;simpleContent&gt;
 *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema&gt;string"&gt;
 *       &lt;attribute name="record-type"&gt;
 *         &lt;simpleType&gt;
 *           &lt;restriction base="{http://www.w3.org/2001/XMLSchema}NMTOKEN"&gt;
 *             &lt;enumeration value="A"/&gt;
 *             &lt;enumeration value="AAAA"/&gt;
 *             &lt;enumeration value="AFSDB"/&gt;
 *             &lt;enumeration value="APL"/&gt;
 *             &lt;enumeration value="AXFR"/&gt;
 *             &lt;enumeration value="CAA"/&gt;
 *             &lt;enumeration value="CERT"/&gt;
 *             &lt;enumeration value="CNAME"/&gt;
 *             &lt;enumeration value="DHCID"/&gt;
 *             &lt;enumeration value="DLV"/&gt;
 *             &lt;enumeration value="DNAME"/&gt;
 *             &lt;enumeration value="DNSKEY"/&gt;
 *             &lt;enumeration value="DS"/&gt;
 *             &lt;enumeration value="HIP"/&gt;
 *             &lt;enumeration value="IXFR"/&gt;
 *             &lt;enumeration value="IPSECKEY"/&gt;
 *             &lt;enumeration value="LOC"/&gt;
 *             &lt;enumeration value="MX"/&gt;
 *             &lt;enumeration value="NAPTR"/&gt;
 *             &lt;enumeration value="NS"/&gt;
 *             &lt;enumeration value="NSEC"/&gt;
 *             &lt;enumeration value="NSEC3"/&gt;
 *             &lt;enumeration value="NSEC3PARAM"/&gt;
 *             &lt;enumeration value="OPT"/&gt;
 *             &lt;enumeration value="PTR"/&gt;
 *             &lt;enumeration value="RRSIG"/&gt;
 *             &lt;enumeration value="RP"/&gt;
 *             &lt;enumeration value="SIG"/&gt;
 *             &lt;enumeration value="SOA"/&gt;
 *             &lt;enumeration value="SPF"/&gt;
 *             &lt;enumeration value="SRV"/&gt;
 *             &lt;enumeration value="SSHFP"/&gt;
 *             &lt;enumeration value="TA"/&gt;
 *             &lt;enumeration value="TKEY"/&gt;
 *             &lt;enumeration value="TLSA"/&gt;
 *             &lt;enumeration value="TSIG"/&gt;
 *             &lt;enumeration value="TXT"/&gt;
 *           &lt;/restriction&gt;
 *         &lt;/simpleType&gt;
 *       &lt;/attribute&gt;
 *     &lt;/extension&gt;
 *   &lt;/simpleContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "value"
})
@XmlRootElement(name = "RelatedDNS")
public class RelatedDNS {

    @XmlValue
    protected String value;
    @XmlAttribute(name = "record-type")
    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    protected String recordType;

    /**
     * Gets the value of the value property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getValue() {
        return value;
    }

    /**
     * Sets the value of the value property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setValue(String value) {
        this.value = value;
    }

    /**
     * Gets the value of the recordType property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getRecordType() {
        return recordType;
    }

    /**
     * Sets the value of the recordType property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setRecordType(String value) {
        this.recordType = value;
    }

}
