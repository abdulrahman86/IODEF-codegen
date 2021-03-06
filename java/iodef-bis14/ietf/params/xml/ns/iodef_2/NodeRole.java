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


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType&gt;
 *   &lt;simpleContent&gt;
 *     &lt;extension base="&lt;urn:ietf:params:xml:ns:iodef-2.0&gt;MLStringType"&gt;
 *       &lt;attribute name="category" use="required" type="{urn:ietf:params:xml:ns:iodef-2.0}noderole-category-type" /&gt;
 *       &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" /&gt;
 *     &lt;/extension&gt;
 *   &lt;/simpleContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "")
@XmlRootElement(name = "NodeRole")
public class NodeRole
    extends MLStringType
{

    @XmlAttribute(name = "category", required = true)
    protected NoderoleCategoryType category;
    @XmlAttribute(name = "ext-category")
    protected String extCategory;

    /**
     * Gets the value of the category property.
     * 
     * @return
     *     possible object is
     *     {@link NoderoleCategoryType }
     *     
     */
    public NoderoleCategoryType getCategory() {
        return category;
    }

    /**
     * Sets the value of the category property.
     * 
     * @param value
     *     allowed object is
     *     {@link NoderoleCategoryType }
     *     
     */
    public void setCategory(NoderoleCategoryType value) {
        this.category = value;
    }

    /**
     * Gets the value of the extCategory property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getExtCategory() {
        return extCategory;
    }

    /**
     * Sets the value of the extCategory property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setExtCategory(String value) {
        this.extCategory = value;
    }

}
