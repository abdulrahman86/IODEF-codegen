//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.11 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2015.07.23 at 09:39:40 PM JST 
//


package ietf.params.xml.ns.iodef_2;

import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElementRef;
import javax.xml.bind.annotation.XmlElementRefs;
import javax.xml.bind.annotation.XmlID;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.adapters.CollapsedStringAdapter;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;


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
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}IncidentCategory" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;choice maxOccurs="unbounded"&gt;
 *           &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}SystemImpact"/&gt;
 *           &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}BusinessImpact"/&gt;
 *           &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}TimeImpact"/&gt;
 *           &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}MonetaryImpact"/&gt;
 *           &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}IntendedImpact"/&gt;
 *         &lt;/choice&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Counter" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}MitigatingFactor" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Confidence" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}AdditionalData" maxOccurs="unbounded" minOccurs="0"/&gt;
 *       &lt;/sequence&gt;
 *       &lt;attribute name="occurrence"&gt;
 *         &lt;simpleType&gt;
 *           &lt;restriction base="{http://www.w3.org/2001/XMLSchema}NMTOKEN"&gt;
 *             &lt;enumeration value="actual"/&gt;
 *             &lt;enumeration value="potential"/&gt;
 *           &lt;/restriction&gt;
 *         &lt;/simpleType&gt;
 *       &lt;/attribute&gt;
 *       &lt;attribute name="restriction" type="{urn:ietf:params:xml:ns:iodef-2.0}restriction-type" /&gt;
 *       &lt;attribute name="ext-restriction" type="{http://www.w3.org/2001/XMLSchema}string" /&gt;
 *       &lt;attribute name="observable-id" type="{http://www.w3.org/2001/XMLSchema}ID" /&gt;
 *     &lt;/restriction&gt;
 *   &lt;/complexContent&gt;
 * &lt;/complexType&gt;
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "incidentCategory",
    "systemImpactOrBusinessImpactOrTimeImpact",
    "counter",
    "mitigatingFactor",
    "confidence",
    "additionalData"
})
@XmlRootElement(name = "Assessment")
public class Assessment {

    @XmlElement(name = "IncidentCategory")
    protected List<MLStringType> incidentCategory;
    @XmlElementRefs({
        @XmlElementRef(name = "SystemImpact", namespace = "urn:ietf:params:xml:ns:iodef-2.0", type = SystemImpact.class, required = false),
        @XmlElementRef(name = "IntendedImpact", namespace = "urn:ietf:params:xml:ns:iodef-2.0", type = JAXBElement.class, required = false),
        @XmlElementRef(name = "MonetaryImpact", namespace = "urn:ietf:params:xml:ns:iodef-2.0", type = MonetaryImpact.class, required = false),
        @XmlElementRef(name = "BusinessImpact", namespace = "urn:ietf:params:xml:ns:iodef-2.0", type = JAXBElement.class, required = false),
        @XmlElementRef(name = "TimeImpact", namespace = "urn:ietf:params:xml:ns:iodef-2.0", type = TimeImpact.class, required = false)
    })
    protected List<Object> systemImpactOrBusinessImpactOrTimeImpact;
    @XmlElement(name = "Counter")
    protected List<Counter> counter;
    @XmlElement(name = "MitigatingFactor")
    protected List<MLStringType> mitigatingFactor;
    @XmlElement(name = "Confidence")
    protected Confidence confidence;
    @XmlElement(name = "AdditionalData")
    protected List<ExtensionType> additionalData;
    @XmlAttribute(name = "occurrence")
    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    protected String occurrence;
    @XmlAttribute(name = "restriction")
    protected RestrictionType restriction;
    @XmlAttribute(name = "ext-restriction")
    protected String extRestriction;
    @XmlAttribute(name = "observable-id")
    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    @XmlID
    @XmlSchemaType(name = "ID")
    protected String observableId;

    /**
     * Gets the value of the incidentCategory property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the incidentCategory property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getIncidentCategory().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link MLStringType }
     * 
     * 
     */
    public List<MLStringType> getIncidentCategory() {
        if (incidentCategory == null) {
            incidentCategory = new ArrayList<MLStringType>();
        }
        return this.incidentCategory;
    }

    /**
     * Gets the value of the systemImpactOrBusinessImpactOrTimeImpact property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the systemImpactOrBusinessImpactOrTimeImpact property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getSystemImpactOrBusinessImpactOrTimeImpact().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link SystemImpact }
     * {@link JAXBElement }{@code <}{@link BusinessImpactType }{@code >}
     * {@link TimeImpact }
     * {@link MonetaryImpact }
     * {@link JAXBElement }{@code <}{@link BusinessImpactType }{@code >}
     * 
     * 
     */
    public List<Object> getSystemImpactOrBusinessImpactOrTimeImpact() {
        if (systemImpactOrBusinessImpactOrTimeImpact == null) {
            systemImpactOrBusinessImpactOrTimeImpact = new ArrayList<Object>();
        }
        return this.systemImpactOrBusinessImpactOrTimeImpact;
    }

    /**
     * Gets the value of the counter property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the counter property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getCounter().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link Counter }
     * 
     * 
     */
    public List<Counter> getCounter() {
        if (counter == null) {
            counter = new ArrayList<Counter>();
        }
        return this.counter;
    }

    /**
     * Gets the value of the mitigatingFactor property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the mitigatingFactor property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getMitigatingFactor().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link MLStringType }
     * 
     * 
     */
    public List<MLStringType> getMitigatingFactor() {
        if (mitigatingFactor == null) {
            mitigatingFactor = new ArrayList<MLStringType>();
        }
        return this.mitigatingFactor;
    }

    /**
     * Gets the value of the confidence property.
     * 
     * @return
     *     possible object is
     *     {@link Confidence }
     *     
     */
    public Confidence getConfidence() {
        return confidence;
    }

    /**
     * Sets the value of the confidence property.
     * 
     * @param value
     *     allowed object is
     *     {@link Confidence }
     *     
     */
    public void setConfidence(Confidence value) {
        this.confidence = value;
    }

    /**
     * Gets the value of the additionalData property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the additionalData property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getAdditionalData().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link ExtensionType }
     * 
     * 
     */
    public List<ExtensionType> getAdditionalData() {
        if (additionalData == null) {
            additionalData = new ArrayList<ExtensionType>();
        }
        return this.additionalData;
    }

    /**
     * Gets the value of the occurrence property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getOccurrence() {
        return occurrence;
    }

    /**
     * Sets the value of the occurrence property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setOccurrence(String value) {
        this.occurrence = value;
    }

    /**
     * Gets the value of the restriction property.
     * 
     * @return
     *     possible object is
     *     {@link RestrictionType }
     *     
     */
    public RestrictionType getRestriction() {
        return restriction;
    }

    /**
     * Sets the value of the restriction property.
     * 
     * @param value
     *     allowed object is
     *     {@link RestrictionType }
     *     
     */
    public void setRestriction(RestrictionType value) {
        this.restriction = value;
    }

    /**
     * Gets the value of the extRestriction property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getExtRestriction() {
        return extRestriction;
    }

    /**
     * Sets the value of the extRestriction property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setExtRestriction(String value) {
        this.extRestriction = value;
    }

    /**
     * Gets the value of the observableId property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getObservableId() {
        return observableId;
    }

    /**
     * Sets the value of the observableId property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setObservableId(String value) {
        this.observableId = value;
    }

}
