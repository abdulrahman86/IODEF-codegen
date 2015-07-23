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
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlID;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.adapters.CollapsedStringAdapter;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import javax.xml.datatype.XMLGregorianCalendar;


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
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Description" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}DetectTime" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}StartTime" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}EndTime" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}RecoveryTime" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}ReportTime" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Contact" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Discovery" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Assessment" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Method" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Flow" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Expectation" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}Record" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}EventData" maxOccurs="unbounded" minOccurs="0"/&gt;
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-2.0}AdditionalData" maxOccurs="unbounded" minOccurs="0"/&gt;
 *       &lt;/sequence&gt;
 *       &lt;attribute name="restriction" type="{urn:ietf:params:xml:ns:iodef-2.0}restriction-type" default="default" /&gt;
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
    "description",
    "detectTime",
    "startTime",
    "endTime",
    "recoveryTime",
    "reportTime",
    "contact",
    "discovery",
    "assessment",
    "method",
    "flow",
    "expectation",
    "record",
    "eventData",
    "additionalData"
})
@XmlRootElement(name = "EventData")
public class EventData {

    @XmlElement(name = "Description")
    protected List<MLStringType> description;
    @XmlElement(name = "DetectTime")
    @XmlSchemaType(name = "dateTime")
    protected XMLGregorianCalendar detectTime;
    @XmlElement(name = "StartTime")
    @XmlSchemaType(name = "dateTime")
    protected XMLGregorianCalendar startTime;
    @XmlElement(name = "EndTime")
    @XmlSchemaType(name = "dateTime")
    protected XMLGregorianCalendar endTime;
    @XmlElement(name = "RecoveryTime")
    @XmlSchemaType(name = "dateTime")
    protected XMLGregorianCalendar recoveryTime;
    @XmlElement(name = "ReportTime")
    @XmlSchemaType(name = "dateTime")
    protected XMLGregorianCalendar reportTime;
    @XmlElement(name = "Contact")
    protected List<Contact> contact;
    @XmlElement(name = "Discovery")
    protected List<Discovery> discovery;
    @XmlElement(name = "Assessment")
    protected Assessment assessment;
    @XmlElement(name = "Method")
    protected List<Method> method;
    @XmlElement(name = "Flow")
    protected List<Flow> flow;
    @XmlElement(name = "Expectation")
    protected List<Expectation> expectation;
    @XmlElement(name = "Record")
    protected Record record;
    @XmlElement(name = "EventData")
    protected List<EventData> eventData;
    @XmlElement(name = "AdditionalData")
    protected List<ExtensionType> additionalData;
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

    /**
     * Gets the value of the detectTime property.
     * 
     * @return
     *     possible object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public XMLGregorianCalendar getDetectTime() {
        return detectTime;
    }

    /**
     * Sets the value of the detectTime property.
     * 
     * @param value
     *     allowed object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public void setDetectTime(XMLGregorianCalendar value) {
        this.detectTime = value;
    }

    /**
     * Gets the value of the startTime property.
     * 
     * @return
     *     possible object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public XMLGregorianCalendar getStartTime() {
        return startTime;
    }

    /**
     * Sets the value of the startTime property.
     * 
     * @param value
     *     allowed object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public void setStartTime(XMLGregorianCalendar value) {
        this.startTime = value;
    }

    /**
     * Gets the value of the endTime property.
     * 
     * @return
     *     possible object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public XMLGregorianCalendar getEndTime() {
        return endTime;
    }

    /**
     * Sets the value of the endTime property.
     * 
     * @param value
     *     allowed object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public void setEndTime(XMLGregorianCalendar value) {
        this.endTime = value;
    }

    /**
     * Gets the value of the recoveryTime property.
     * 
     * @return
     *     possible object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public XMLGregorianCalendar getRecoveryTime() {
        return recoveryTime;
    }

    /**
     * Sets the value of the recoveryTime property.
     * 
     * @param value
     *     allowed object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public void setRecoveryTime(XMLGregorianCalendar value) {
        this.recoveryTime = value;
    }

    /**
     * Gets the value of the reportTime property.
     * 
     * @return
     *     possible object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public XMLGregorianCalendar getReportTime() {
        return reportTime;
    }

    /**
     * Sets the value of the reportTime property.
     * 
     * @param value
     *     allowed object is
     *     {@link XMLGregorianCalendar }
     *     
     */
    public void setReportTime(XMLGregorianCalendar value) {
        this.reportTime = value;
    }

    /**
     * Gets the value of the contact property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the contact property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getContact().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link Contact }
     * 
     * 
     */
    public List<Contact> getContact() {
        if (contact == null) {
            contact = new ArrayList<Contact>();
        }
        return this.contact;
    }

    /**
     * Gets the value of the discovery property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the discovery property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getDiscovery().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link Discovery }
     * 
     * 
     */
    public List<Discovery> getDiscovery() {
        if (discovery == null) {
            discovery = new ArrayList<Discovery>();
        }
        return this.discovery;
    }

    /**
     * Gets the value of the assessment property.
     * 
     * @return
     *     possible object is
     *     {@link Assessment }
     *     
     */
    public Assessment getAssessment() {
        return assessment;
    }

    /**
     * Sets the value of the assessment property.
     * 
     * @param value
     *     allowed object is
     *     {@link Assessment }
     *     
     */
    public void setAssessment(Assessment value) {
        this.assessment = value;
    }

    /**
     * Gets the value of the method property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the method property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getMethod().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link Method }
     * 
     * 
     */
    public List<Method> getMethod() {
        if (method == null) {
            method = new ArrayList<Method>();
        }
        return this.method;
    }

    /**
     * Gets the value of the flow property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the flow property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getFlow().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link Flow }
     * 
     * 
     */
    public List<Flow> getFlow() {
        if (flow == null) {
            flow = new ArrayList<Flow>();
        }
        return this.flow;
    }

    /**
     * Gets the value of the expectation property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the expectation property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getExpectation().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link Expectation }
     * 
     * 
     */
    public List<Expectation> getExpectation() {
        if (expectation == null) {
            expectation = new ArrayList<Expectation>();
        }
        return this.expectation;
    }

    /**
     * Gets the value of the record property.
     * 
     * @return
     *     possible object is
     *     {@link Record }
     *     
     */
    public Record getRecord() {
        return record;
    }

    /**
     * Sets the value of the record property.
     * 
     * @param value
     *     allowed object is
     *     {@link Record }
     *     
     */
    public void setRecord(Record value) {
        this.record = value;
    }

    /**
     * Gets the value of the eventData property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the eventData property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getEventData().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link EventData }
     * 
     * 
     */
    public List<EventData> getEventData() {
        if (eventData == null) {
            eventData = new ArrayList<EventData>();
        }
        return this.eventData;
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
     * Gets the value of the restriction property.
     * 
     * @return
     *     possible object is
     *     {@link RestrictionType }
     *     
     */
    public RestrictionType getRestriction() {
        if (restriction == null) {
            return RestrictionType.DEFAULT;
        } else {
            return restriction;
        }
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
