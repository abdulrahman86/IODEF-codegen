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
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
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
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}BulkObservableFormat" minOccurs="0"/&gt;
 *         &lt;element name="BulkObservableList" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/&gt;
 *       &lt;/sequence&gt;
 *       &lt;attribute name="type" use="required" type="{urn:ietf:params:xml:ns:iodef-2.0}observable-type-type" /&gt;
 *       &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" /&gt;
 *     &lt;/restriction&gt;
 *   &lt;/complexContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "bulkObservableFormat",
    "bulkObservableList"
})
@XmlRootElement(name = "BulkObservable")
public class BulkObservable {

    @XmlElement(name = "BulkObservableFormat")
    protected BulkObservableFormat bulkObservableFormat;
    @XmlElement(name = "BulkObservableList")
    protected String bulkObservableList;
    @XmlAttribute(name = "type", required = true)
    protected ObservableTypeType type;
    @XmlAttribute(name = "ext-type")
    protected String extType;

    /**
     * Gets the value of the bulkObservableFormat property.
     * 
     * @return
     *     possible object is
     *     {@link BulkObservableFormat }
     *     
     */
    public BulkObservableFormat getBulkObservableFormat() {
        return bulkObservableFormat;
    }

    /**
     * Sets the value of the bulkObservableFormat property.
     * 
     * @param value
     *     allowed object is
     *     {@link BulkObservableFormat }
     *     
     */
    public void setBulkObservableFormat(BulkObservableFormat value) {
        this.bulkObservableFormat = value;
    }

    /**
     * Gets the value of the bulkObservableList property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getBulkObservableList() {
        return bulkObservableList;
    }

    /**
     * Sets the value of the bulkObservableList property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setBulkObservableList(String value) {
        this.bulkObservableList = value;
    }

    /**
     * Gets the value of the type property.
     * 
     * @return
     *     possible object is
     *     {@link ObservableTypeType }
     *     
     */
    public ObservableTypeType getType() {
        return type;
    }

    /**
     * Sets the value of the type property.
     * 
     * @param value
     *     allowed object is
     *     {@link ObservableTypeType }
     *     
     */
    public void setType(ObservableTypeType value) {
        this.type = value;
    }

    /**
     * Gets the value of the extType property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getExtType() {
        return extType;
    }

    /**
     * Sets the value of the extType property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setExtType(String value) {
        this.extType = value;
    }

}
