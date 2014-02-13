//
// このファイルは、JavaTM Architecture for XML Binding(JAXB) Reference Implementation、v2.2.7によって生成されました 
// <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a>を参照してください 
// ソース・スキーマの再コンパイル時にこのファイルの変更は失われます。 
// 生成日: 2014.02.11 時間 12:56:35 PM JST 
//


package ietf.params.xml.ns.iodef_1;

import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElements;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>anonymous complex typeのJavaクラス。
 * 
 * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;choice maxOccurs="unbounded" minOccurs="0">
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID"/>
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}Description"/>
 *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IODEF-Document"/>
 *       &lt;/choice>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "incidentIDOrDescriptionOrIODEFDocument"
})
@XmlRootElement(name = "NewDataSet")
public class NewDataSet {

    @XmlElements({
        @XmlElement(name = "IncidentID", type = IncidentID.class, nillable = true),
        @XmlElement(name = "Description", type = Description.class, nillable = true),
        @XmlElement(name = "IODEF-Document", type = IODEFDocument.class)
    })
    protected List<Object> incidentIDOrDescriptionOrIODEFDocument;

    /**
     * Gets the value of the incidentIDOrDescriptionOrIODEFDocument property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the incidentIDOrDescriptionOrIODEFDocument property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getIncidentIDOrDescriptionOrIODEFDocument().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link IncidentID }
     * {@link Description }
     * {@link IODEFDocument }
     * 
     * 
     */
    public List<Object> getIncidentIDOrDescriptionOrIODEFDocument() {
        if (incidentIDOrDescriptionOrIODEFDocument == null) {
            incidentIDOrDescriptionOrIODEFDocument = new ArrayList<Object>();
        }
        return this.incidentIDOrDescriptionOrIODEFDocument;
    }

}
