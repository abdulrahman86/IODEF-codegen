//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.11 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2015.07.23 at 09:39:40 PM JST 
//


package ietf.params.xml.ns.iodef_2;

import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType&gt;
 *   &lt;complexContent&gt;
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType"&gt;
 *       &lt;sequence&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}IANAService"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}URL" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Description" maxOccurs="unbounded" minOccurs="0"/&gt;
 *       &lt;/sequence&gt;
 *     &lt;/restriction&gt;
 *   &lt;/complexContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "ianaService",
    "url",
    "description"
})
@XmlRootElement(name = "ServiceName")
public class ServiceName {

    @XmlElement(name = "IANAService", required = true)
    protected String ianaService;
    @XmlElement(name = "URL")
    @XmlSchemaType(name = "anyURI")
    protected List<String> url;
    @XmlElement(name = "Description")
    protected List<MLStringType> description;

    /**
     * Gets the value of the ianaService property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getIANAService() {
        return ianaService;
    }

    /**
     * Sets the value of the ianaService property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setIANAService(String value) {
        this.ianaService = value;
    }

    /**
     * Gets the value of the url property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the url property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getURL().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link String }
     * 
     * 
     */
    public List<String> getURL() {
        if (url == null) {
            url = new ArrayList<String>();
        }
        return this.url;
    }

    /**
     * Gets the value of the description property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the description property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getDescription().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link MLStringType }
     * 
     * 
     */
    public List<MLStringType> getDescription() {
        if (description == null) {
            description = new ArrayList<MLStringType>();
        }
        return this.description;
    }

}
