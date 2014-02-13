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
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.XmlValue;


/**
 * <p>anonymous complex typeのJavaクラス。
 * 
 * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="Incident" maxOccurs="unbounded" minOccurs="0">
 *           &lt;complexType>
 *             &lt;complexContent>
 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                 &lt;sequence>
 *                   &lt;element name="DetectTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                   &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                   &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                   &lt;element name="ReportTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                   &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
 *                   &lt;element name="AlternativeID" maxOccurs="unbounded" minOccurs="0">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
 *                           &lt;/sequence>
 *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                   &lt;element name="RelatedActivity" maxOccurs="unbounded" minOccurs="0">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
 *                           &lt;/sequence>
 *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                   &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}Description" maxOccurs="unbounded" minOccurs="0"/>
 *                   &lt;element name="Assessment" maxOccurs="unbounded" minOccurs="0">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element name="Impact" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="completion" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="TimeImpact" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="metric" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-metric" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="MonetaryImpact" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="currency" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="Counter" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="Confidence" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="rating" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="AdditionalData" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                           &lt;/sequence>
 *                           &lt;attribute name="occurrence" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                   &lt;element name="Method" maxOccurs="unbounded" minOccurs="0">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element name="Reference" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;complexContent>
 *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                     &lt;sequence>
 *                                       &lt;element name="ReferenceName" maxOccurs="unbounded" minOccurs="0">
 *                                         &lt;complexType>
 *                                           &lt;simpleContent>
 *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                               &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                             &lt;/extension>
 *                                           &lt;/simpleContent>
 *                                         &lt;/complexType>
 *                                       &lt;/element>
 *                                       &lt;element name="URL" maxOccurs="unbounded" minOccurs="0">
 *                                         &lt;complexType>
 *                                           &lt;simpleContent>
 *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                             &lt;/extension>
 *                                           &lt;/simpleContent>
 *                                         &lt;/complexType>
 *                                       &lt;/element>
 *                                     &lt;/sequence>
 *                                   &lt;/restriction>
 *                                 &lt;/complexContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}Description" maxOccurs="unbounded" minOccurs="0"/>
 *                           &lt;/sequence>
 *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                   &lt;element name="Contact" maxOccurs="unbounded" minOccurs="0">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element name="Timezone" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                             &lt;element name="ContactName" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="RegistryHandle" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="registry" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-registry" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="PostalAddress" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="Email" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="Telephone" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="Fax" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;simpleContent>
 *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                     &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/extension>
 *                                 &lt;/simpleContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                           &lt;/sequence>
 *                           &lt;attribute name="role" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                           &lt;attribute name="ext-role" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                           &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                           &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                   &lt;element name="EventData" maxOccurs="unbounded" minOccurs="0">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element name="DetectTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                             &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                             &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                             &lt;element name="Flow" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;complexContent>
 *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                     &lt;sequence>
 *                                       &lt;element name="System" maxOccurs="unbounded" minOccurs="0">
 *                                         &lt;complexType>
 *                                           &lt;complexContent>
 *                                             &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                               &lt;sequence>
 *                                                 &lt;element name="Node" maxOccurs="unbounded" minOccurs="0">
 *                                                   &lt;complexType>
 *                                                     &lt;complexContent>
 *                                                       &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                                         &lt;sequence>
 *                                                           &lt;element name="Counter" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                           &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                           &lt;element name="NodeName" maxOccurs="unbounded" minOccurs="0">
 *                                                             &lt;complexType>
 *                                                               &lt;simpleContent>
 *                                                                 &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                                                   &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                 &lt;/extension>
 *                                                               &lt;/simpleContent>
 *                                                             &lt;/complexType>
 *                                                           &lt;/element>
 *                                                           &lt;element name="Address" maxOccurs="unbounded" minOccurs="0">
 *                                                             &lt;complexType>
 *                                                               &lt;simpleContent>
 *                                                                 &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                                                   &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="vlan-name" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="vlan-num" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                 &lt;/extension>
 *                                                               &lt;/simpleContent>
 *                                                             &lt;/complexType>
 *                                                           &lt;/element>
 *                                                           &lt;element name="Location" maxOccurs="unbounded" minOccurs="0">
 *                                                             &lt;complexType>
 *                                                               &lt;simpleContent>
 *                                                                 &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                                                   &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                 &lt;/extension>
 *                                                               &lt;/simpleContent>
 *                                                             &lt;/complexType>
 *                                                           &lt;/element>
 *                                                           &lt;element name="NodeRole" maxOccurs="unbounded" minOccurs="0">
 *                                                             &lt;complexType>
 *                                                               &lt;simpleContent>
 *                                                                 &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                                                   &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                 &lt;/extension>
 *                                                               &lt;/simpleContent>
 *                                                             &lt;/complexType>
 *                                                           &lt;/element>
 *                                                         &lt;/sequence>
 *                                                       &lt;/restriction>
 *                                                     &lt;/complexContent>
 *                                                   &lt;/complexType>
 *                                                 &lt;/element>
 *                                                 &lt;element name="Service" maxOccurs="unbounded" minOccurs="0">
 *                                                   &lt;complexType>
 *                                                     &lt;complexContent>
 *                                                       &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                                         &lt;sequence>
 *                                                           &lt;element name="Port" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                           &lt;element name="Portlist" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                           &lt;element name="ProtoType" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                           &lt;element name="ProtoCode" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                           &lt;element name="ProtoField" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                           &lt;element name="Application" maxOccurs="unbounded" minOccurs="0">
 *                                                             &lt;complexType>
 *                                                               &lt;complexContent>
 *                                                                 &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                                                   &lt;sequence>
 *                                                                     &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                                   &lt;/sequence>
 *                                                                   &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                   &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                                 &lt;/restriction>
 *                                                               &lt;/complexContent>
 *                                                             &lt;/complexType>
 *                                                           &lt;/element>
 *                                                         &lt;/sequence>
 *                                                         &lt;attribute name="ip_protocol" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                       &lt;/restriction>
 *                                                     &lt;/complexContent>
 *                                                   &lt;/complexType>
 *                                                 &lt;/element>
 *                                                 &lt;element name="OperatingSystem" maxOccurs="unbounded" minOccurs="0">
 *                                                   &lt;complexType>
 *                                                     &lt;complexContent>
 *                                                       &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                                         &lt;sequence>
 *                                                           &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                         &lt;/sequence>
 *                                                         &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                       &lt;/restriction>
 *                                                     &lt;/complexContent>
 *                                                   &lt;/complexType>
 *                                                 &lt;/element>
 *                                               &lt;/sequence>
 *                                               &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                               &lt;attribute name="interface" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                               &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                               &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                               &lt;attribute name="spoofed" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                             &lt;/restriction>
 *                                           &lt;/complexContent>
 *                                         &lt;/complexType>
 *                                       &lt;/element>
 *                                     &lt;/sequence>
 *                                   &lt;/restriction>
 *                                 &lt;/complexContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="Expectation" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;complexContent>
 *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                     &lt;sequence>
 *                                       &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                       &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                     &lt;/sequence>
 *                                     &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/restriction>
 *                                 &lt;/complexContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                             &lt;element name="Record" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;complexContent>
 *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                     &lt;sequence>
 *                                       &lt;element name="RecordData" maxOccurs="unbounded" minOccurs="0">
 *                                         &lt;complexType>
 *                                           &lt;complexContent>
 *                                             &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                               &lt;sequence>
 *                                                 &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                                 &lt;element name="RecordPattern" maxOccurs="unbounded" minOccurs="0">
 *                                                   &lt;complexType>
 *                                                     &lt;simpleContent>
 *                                                       &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                                         &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="offset" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="ext-offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="instance" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                       &lt;/extension>
 *                                                     &lt;/simpleContent>
 *                                                   &lt;/complexType>
 *                                                 &lt;/element>
 *                                                 &lt;element name="RecordItem" maxOccurs="unbounded" minOccurs="0">
 *                                                   &lt;complexType>
 *                                                     &lt;simpleContent>
 *                                                       &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
 *                                                         &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                         &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                                       &lt;/extension>
 *                                                     &lt;/simpleContent>
 *                                                   &lt;/complexType>
 *                                                 &lt;/element>
 *                                               &lt;/sequence>
 *                                               &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                             &lt;/restriction>
 *                                           &lt;/complexContent>
 *                                         &lt;/complexType>
 *                                       &lt;/element>
 *                                     &lt;/sequence>
 *                                     &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/restriction>
 *                                 &lt;/complexContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                           &lt;/sequence>
 *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                   &lt;element name="History" maxOccurs="unbounded" minOccurs="0">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element name="HistoryItem" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;complexContent>
 *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                     &lt;sequence>
 *                                       &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
 *                                     &lt;/sequence>
 *                                     &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                     &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                                   &lt;/restriction>
 *                                 &lt;/complexContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                           &lt;/sequence>
 *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                 &lt;/sequence>
 *                 &lt;attribute name="purpose" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                 &lt;attribute name="ext-purpose" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
 *               &lt;/restriction>
 *             &lt;/complexContent>
 *           &lt;/complexType>
 *         &lt;/element>
 *       &lt;/sequence>
 *       &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
 *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
 *       &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "incident"
})
@XmlRootElement(name = "IODEF-Document")
public class IODEFDocument {

    @XmlElement(name = "Incident")
    protected List<IODEFDocument.Incident> incident;
    @XmlAttribute(name = "version")
    protected String version;
    @XmlAttribute(name = "lang")
    protected String lang;
    @XmlAttribute(name = "formatid")
    protected String formatid;

    /**
     * Gets the value of the incident property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the incident property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getIncident().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link IODEFDocument.Incident }
     * 
     * 
     */
    public List<IODEFDocument.Incident> getIncident() {
        if (incident == null) {
            incident = new ArrayList<IODEFDocument.Incident>();
        }
        return this.incident;
    }

    /**
     * versionプロパティの値を取得します。
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getVersion() {
        return version;
    }

    /**
     * versionプロパティの値を設定します。
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setVersion(String value) {
        this.version = value;
    }

    /**
     * langプロパティの値を取得します。
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getLang() {
        return lang;
    }

    /**
     * langプロパティの値を設定します。
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setLang(String value) {
        this.lang = value;
    }

    /**
     * formatidプロパティの値を取得します。
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getFormatid() {
        return formatid;
    }

    /**
     * formatidプロパティの値を設定します。
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setFormatid(String value) {
        this.formatid = value;
    }


    /**
     * <p>anonymous complex typeのJavaクラス。
     * 
     * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
     * 
     * <pre>
     * &lt;complexType>
     *   &lt;complexContent>
     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *       &lt;sequence>
     *         &lt;element name="DetectTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *         &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *         &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *         &lt;element name="ReportTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
     *         &lt;element name="AlternativeID" maxOccurs="unbounded" minOccurs="0">
     *           &lt;complexType>
     *             &lt;complexContent>
     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                 &lt;sequence>
     *                   &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
     *                 &lt;/sequence>
     *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/restriction>
     *             &lt;/complexContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *         &lt;element name="RelatedActivity" maxOccurs="unbounded" minOccurs="0">
     *           &lt;complexType>
     *             &lt;complexContent>
     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                 &lt;sequence>
     *                   &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
     *                 &lt;/sequence>
     *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/restriction>
     *             &lt;/complexContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}Description" maxOccurs="unbounded" minOccurs="0"/>
     *         &lt;element name="Assessment" maxOccurs="unbounded" minOccurs="0">
     *           &lt;complexType>
     *             &lt;complexContent>
     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                 &lt;sequence>
     *                   &lt;element name="Impact" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="completion" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="TimeImpact" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="metric" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-metric" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="MonetaryImpact" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="currency" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="Counter" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="Confidence" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="rating" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="AdditionalData" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                 &lt;/sequence>
     *                 &lt;attribute name="occurrence" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/restriction>
     *             &lt;/complexContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *         &lt;element name="Method" maxOccurs="unbounded" minOccurs="0">
     *           &lt;complexType>
     *             &lt;complexContent>
     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                 &lt;sequence>
     *                   &lt;element name="Reference" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;complexContent>
     *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                           &lt;sequence>
     *                             &lt;element name="ReferenceName" maxOccurs="unbounded" minOccurs="0">
     *                               &lt;complexType>
     *                                 &lt;simpleContent>
     *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                     &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                   &lt;/extension>
     *                                 &lt;/simpleContent>
     *                               &lt;/complexType>
     *                             &lt;/element>
     *                             &lt;element name="URL" maxOccurs="unbounded" minOccurs="0">
     *                               &lt;complexType>
     *                                 &lt;simpleContent>
     *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                   &lt;/extension>
     *                                 &lt;/simpleContent>
     *                               &lt;/complexType>
     *                             &lt;/element>
     *                           &lt;/sequence>
     *                         &lt;/restriction>
     *                       &lt;/complexContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}Description" maxOccurs="unbounded" minOccurs="0"/>
     *                 &lt;/sequence>
     *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/restriction>
     *             &lt;/complexContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *         &lt;element name="Contact" maxOccurs="unbounded" minOccurs="0">
     *           &lt;complexType>
     *             &lt;complexContent>
     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                 &lt;sequence>
     *                   &lt;element name="Timezone" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                   &lt;element name="ContactName" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="RegistryHandle" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="registry" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-registry" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="PostalAddress" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="Email" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="Telephone" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="Fax" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;simpleContent>
     *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                           &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/extension>
     *                       &lt;/simpleContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                 &lt;/sequence>
     *                 &lt;attribute name="role" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                 &lt;attribute name="ext-role" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                 &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                 &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/restriction>
     *             &lt;/complexContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *         &lt;element name="EventData" maxOccurs="unbounded" minOccurs="0">
     *           &lt;complexType>
     *             &lt;complexContent>
     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                 &lt;sequence>
     *                   &lt;element name="DetectTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                   &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                   &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                   &lt;element name="Flow" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;complexContent>
     *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                           &lt;sequence>
     *                             &lt;element name="System" maxOccurs="unbounded" minOccurs="0">
     *                               &lt;complexType>
     *                                 &lt;complexContent>
     *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                                     &lt;sequence>
     *                                       &lt;element name="Node" maxOccurs="unbounded" minOccurs="0">
     *                                         &lt;complexType>
     *                                           &lt;complexContent>
     *                                             &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                                               &lt;sequence>
     *                                                 &lt;element name="Counter" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                 &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                 &lt;element name="NodeName" maxOccurs="unbounded" minOccurs="0">
     *                                                   &lt;complexType>
     *                                                     &lt;simpleContent>
     *                                                       &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                                         &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                       &lt;/extension>
     *                                                     &lt;/simpleContent>
     *                                                   &lt;/complexType>
     *                                                 &lt;/element>
     *                                                 &lt;element name="Address" maxOccurs="unbounded" minOccurs="0">
     *                                                   &lt;complexType>
     *                                                     &lt;simpleContent>
     *                                                       &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                                         &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="vlan-name" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="vlan-num" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                       &lt;/extension>
     *                                                     &lt;/simpleContent>
     *                                                   &lt;/complexType>
     *                                                 &lt;/element>
     *                                                 &lt;element name="Location" maxOccurs="unbounded" minOccurs="0">
     *                                                   &lt;complexType>
     *                                                     &lt;simpleContent>
     *                                                       &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                                         &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                       &lt;/extension>
     *                                                     &lt;/simpleContent>
     *                                                   &lt;/complexType>
     *                                                 &lt;/element>
     *                                                 &lt;element name="NodeRole" maxOccurs="unbounded" minOccurs="0">
     *                                                   &lt;complexType>
     *                                                     &lt;simpleContent>
     *                                                       &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                                         &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                       &lt;/extension>
     *                                                     &lt;/simpleContent>
     *                                                   &lt;/complexType>
     *                                                 &lt;/element>
     *                                               &lt;/sequence>
     *                                             &lt;/restriction>
     *                                           &lt;/complexContent>
     *                                         &lt;/complexType>
     *                                       &lt;/element>
     *                                       &lt;element name="Service" maxOccurs="unbounded" minOccurs="0">
     *                                         &lt;complexType>
     *                                           &lt;complexContent>
     *                                             &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                                               &lt;sequence>
     *                                                 &lt;element name="Port" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                 &lt;element name="Portlist" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                 &lt;element name="ProtoType" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                 &lt;element name="ProtoCode" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                 &lt;element name="ProtoField" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                 &lt;element name="Application" maxOccurs="unbounded" minOccurs="0">
     *                                                   &lt;complexType>
     *                                                     &lt;complexContent>
     *                                                       &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                                                         &lt;sequence>
     *                                                           &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                                         &lt;/sequence>
     *                                                         &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                         &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                                       &lt;/restriction>
     *                                                     &lt;/complexContent>
     *                                                   &lt;/complexType>
     *                                                 &lt;/element>
     *                                               &lt;/sequence>
     *                                               &lt;attribute name="ip_protocol" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                             &lt;/restriction>
     *                                           &lt;/complexContent>
     *                                         &lt;/complexType>
     *                                       &lt;/element>
     *                                       &lt;element name="OperatingSystem" maxOccurs="unbounded" minOccurs="0">
     *                                         &lt;complexType>
     *                                           &lt;complexContent>
     *                                             &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                                               &lt;sequence>
     *                                                 &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                               &lt;/sequence>
     *                                               &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                             &lt;/restriction>
     *                                           &lt;/complexContent>
     *                                         &lt;/complexType>
     *                                       &lt;/element>
     *                                     &lt;/sequence>
     *                                     &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                     &lt;attribute name="interface" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                     &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                     &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                     &lt;attribute name="spoofed" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                   &lt;/restriction>
     *                                 &lt;/complexContent>
     *                               &lt;/complexType>
     *                             &lt;/element>
     *                           &lt;/sequence>
     *                         &lt;/restriction>
     *                       &lt;/complexContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="Expectation" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;complexContent>
     *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                           &lt;sequence>
     *                             &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                             &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                           &lt;/sequence>
     *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/restriction>
     *                       &lt;/complexContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                   &lt;element name="Record" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;complexContent>
     *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                           &lt;sequence>
     *                             &lt;element name="RecordData" maxOccurs="unbounded" minOccurs="0">
     *                               &lt;complexType>
     *                                 &lt;complexContent>
     *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                                     &lt;sequence>
     *                                       &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                                       &lt;element name="RecordPattern" maxOccurs="unbounded" minOccurs="0">
     *                                         &lt;complexType>
     *                                           &lt;simpleContent>
     *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                               &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="offset" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="ext-offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="instance" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                             &lt;/extension>
     *                                           &lt;/simpleContent>
     *                                         &lt;/complexType>
     *                                       &lt;/element>
     *                                       &lt;element name="RecordItem" maxOccurs="unbounded" minOccurs="0">
     *                                         &lt;complexType>
     *                                           &lt;simpleContent>
     *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
     *                                               &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                               &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                             &lt;/extension>
     *                                           &lt;/simpleContent>
     *                                         &lt;/complexType>
     *                                       &lt;/element>
     *                                     &lt;/sequence>
     *                                     &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                                   &lt;/restriction>
     *                                 &lt;/complexContent>
     *                               &lt;/complexType>
     *                             &lt;/element>
     *                           &lt;/sequence>
     *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/restriction>
     *                       &lt;/complexContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                 &lt;/sequence>
     *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/restriction>
     *             &lt;/complexContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *         &lt;element name="History" maxOccurs="unbounded" minOccurs="0">
     *           &lt;complexType>
     *             &lt;complexContent>
     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                 &lt;sequence>
     *                   &lt;element name="HistoryItem" maxOccurs="unbounded" minOccurs="0">
     *                     &lt;complexType>
     *                       &lt;complexContent>
     *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *                           &lt;sequence>
     *                             &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
     *                           &lt;/sequence>
     *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                           &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
     *                         &lt;/restriction>
     *                       &lt;/complexContent>
     *                     &lt;/complexType>
     *                   &lt;/element>
     *                 &lt;/sequence>
     *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *               &lt;/restriction>
     *             &lt;/complexContent>
     *           &lt;/complexType>
     *         &lt;/element>
     *       &lt;/sequence>
     *       &lt;attribute name="purpose" type="{http://www.w3.org/2001/XMLSchema}string" />
     *       &lt;attribute name="ext-purpose" type="{http://www.w3.org/2001/XMLSchema}string" />
     *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
     *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
     *     &lt;/restriction>
     *   &lt;/complexContent>
     * &lt;/complexType>
     * </pre>
     * 
     * 
     */
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "", propOrder = {
        "detectTime",
        "startTime",
        "endTime",
        "reportTime",
        "incidentID",
        "alternativeID",
        "relatedActivity",
        "description",
        "assessment",
        "method",
        "contact",
        "eventData",
        "history"
    })
    public static class Incident {

        @XmlElement(name = "DetectTime")
        protected String detectTime;
        @XmlElement(name = "StartTime")
        protected String startTime;
        @XmlElement(name = "EndTime")
        protected String endTime;
        @XmlElement(name = "ReportTime")
        protected String reportTime;
        @XmlElement(name = "IncidentID", nillable = true)
        protected List<IncidentID> incidentID;
        @XmlElement(name = "AlternativeID")
        protected List<IODEFDocument.Incident.AlternativeID> alternativeID;
        @XmlElement(name = "RelatedActivity")
        protected List<IODEFDocument.Incident.RelatedActivity> relatedActivity;
        @XmlElement(name = "Description", nillable = true)
        protected List<Description> description;
        @XmlElement(name = "Assessment")
        protected List<IODEFDocument.Incident.Assessment> assessment;
        @XmlElement(name = "Method")
        protected List<IODEFDocument.Incident.Method> method;
        @XmlElement(name = "Contact")
        protected List<IODEFDocument.Incident.Contact> contact;
        @XmlElement(name = "EventData")
        protected List<IODEFDocument.Incident.EventData> eventData;
        @XmlElement(name = "History")
        protected List<IODEFDocument.Incident.History> history;
        @XmlAttribute(name = "purpose")
        protected String purpose;
        @XmlAttribute(name = "ext-purpose")
        protected String extPurpose;
        @XmlAttribute(name = "lang")
        protected String lang;
        @XmlAttribute(name = "restriction")
        protected String restriction;

        /**
         * detectTimeプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getDetectTime() {
            return detectTime;
        }

        /**
         * detectTimeプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setDetectTime(String value) {
            this.detectTime = value;
        }

        /**
         * startTimeプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getStartTime() {
            return startTime;
        }

        /**
         * startTimeプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setStartTime(String value) {
            this.startTime = value;
        }

        /**
         * endTimeプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getEndTime() {
            return endTime;
        }

        /**
         * endTimeプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setEndTime(String value) {
            this.endTime = value;
        }

        /**
         * reportTimeプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getReportTime() {
            return reportTime;
        }

        /**
         * reportTimeプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setReportTime(String value) {
            this.reportTime = value;
        }

        /**
         * Gets the value of the incidentID property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the incidentID property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getIncidentID().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link IncidentID }
         * 
         * 
         */
        public List<IncidentID> getIncidentID() {
            if (incidentID == null) {
                incidentID = new ArrayList<IncidentID>();
            }
            return this.incidentID;
        }

        /**
         * Gets the value of the alternativeID property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the alternativeID property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getAlternativeID().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link IODEFDocument.Incident.AlternativeID }
         * 
         * 
         */
        public List<IODEFDocument.Incident.AlternativeID> getAlternativeID() {
            if (alternativeID == null) {
                alternativeID = new ArrayList<IODEFDocument.Incident.AlternativeID>();
            }
            return this.alternativeID;
        }

        /**
         * Gets the value of the relatedActivity property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the relatedActivity property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getRelatedActivity().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link IODEFDocument.Incident.RelatedActivity }
         * 
         * 
         */
        public List<IODEFDocument.Incident.RelatedActivity> getRelatedActivity() {
            if (relatedActivity == null) {
                relatedActivity = new ArrayList<IODEFDocument.Incident.RelatedActivity>();
            }
            return this.relatedActivity;
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
         * {@link Description }
         * 
         * 
         */
        public List<Description> getDescription() {
            if (description == null) {
                description = new ArrayList<Description>();
            }
            return this.description;
        }

        /**
         * Gets the value of the assessment property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the assessment property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getAssessment().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link IODEFDocument.Incident.Assessment }
         * 
         * 
         */
        public List<IODEFDocument.Incident.Assessment> getAssessment() {
            if (assessment == null) {
                assessment = new ArrayList<IODEFDocument.Incident.Assessment>();
            }
            return this.assessment;
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
         * {@link IODEFDocument.Incident.Method }
         * 
         * 
         */
        public List<IODEFDocument.Incident.Method> getMethod() {
            if (method == null) {
                method = new ArrayList<IODEFDocument.Incident.Method>();
            }
            return this.method;
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
         * {@link IODEFDocument.Incident.Contact }
         * 
         * 
         */
        public List<IODEFDocument.Incident.Contact> getContact() {
            if (contact == null) {
                contact = new ArrayList<IODEFDocument.Incident.Contact>();
            }
            return this.contact;
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
         * {@link IODEFDocument.Incident.EventData }
         * 
         * 
         */
        public List<IODEFDocument.Incident.EventData> getEventData() {
            if (eventData == null) {
                eventData = new ArrayList<IODEFDocument.Incident.EventData>();
            }
            return this.eventData;
        }

        /**
         * Gets the value of the history property.
         * 
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the history property.
         * 
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getHistory().add(newItem);
         * </pre>
         * 
         * 
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link IODEFDocument.Incident.History }
         * 
         * 
         */
        public List<IODEFDocument.Incident.History> getHistory() {
            if (history == null) {
                history = new ArrayList<IODEFDocument.Incident.History>();
            }
            return this.history;
        }

        /**
         * purposeプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getPurpose() {
            return purpose;
        }

        /**
         * purposeプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setPurpose(String value) {
            this.purpose = value;
        }

        /**
         * extPurposeプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getExtPurpose() {
            return extPurpose;
        }

        /**
         * extPurposeプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setExtPurpose(String value) {
            this.extPurpose = value;
        }

        /**
         * langプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getLang() {
            return lang;
        }

        /**
         * langプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setLang(String value) {
            this.lang = value;
        }

        /**
         * restrictionプロパティの値を取得します。
         * 
         * @return
         *     possible object is
         *     {@link String }
         *     
         */
        public String getRestriction() {
            return restriction;
        }

        /**
         * restrictionプロパティの値を設定します。
         * 
         * @param value
         *     allowed object is
         *     {@link String }
         *     
         */
        public void setRestriction(String value) {
            this.restriction = value;
        }


        /**
         * <p>anonymous complex typeのJavaクラス。
         * 
         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;complexContent>
         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *       &lt;sequence>
         *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
         *       &lt;/sequence>
         *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/restriction>
         *   &lt;/complexContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "", propOrder = {
            "incidentID"
        })
        public static class AlternativeID {

            @XmlElement(name = "IncidentID", nillable = true)
            protected List<IncidentID> incidentID;
            @XmlAttribute(name = "restriction")
            protected String restriction;

            /**
             * Gets the value of the incidentID property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the incidentID property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getIncidentID().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IncidentID }
             * 
             * 
             */
            public List<IncidentID> getIncidentID() {
                if (incidentID == null) {
                    incidentID = new ArrayList<IncidentID>();
                }
                return this.incidentID;
            }

            /**
             * restrictionプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRestriction() {
                return restriction;
            }

            /**
             * restrictionプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRestriction(String value) {
                this.restriction = value;
            }

        }


        /**
         * <p>anonymous complex typeのJavaクラス。
         * 
         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;complexContent>
         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *       &lt;sequence>
         *         &lt;element name="Impact" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="completion" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="TimeImpact" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="metric" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-metric" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="MonetaryImpact" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="currency" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="Counter" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="Confidence" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="rating" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="AdditionalData" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *       &lt;/sequence>
         *       &lt;attribute name="occurrence" type="{http://www.w3.org/2001/XMLSchema}string" />
         *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/restriction>
         *   &lt;/complexContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "", propOrder = {
            "impact",
            "timeImpact",
            "monetaryImpact",
            "counter",
            "confidence",
            "additionalData"
        })
        public static class Assessment {

            @XmlElement(name = "Impact", nillable = true)
            protected List<IODEFDocument.Incident.Assessment.Impact> impact;
            @XmlElement(name = "TimeImpact", nillable = true)
            protected List<IODEFDocument.Incident.Assessment.TimeImpact> timeImpact;
            @XmlElement(name = "MonetaryImpact", nillable = true)
            protected List<IODEFDocument.Incident.Assessment.MonetaryImpact> monetaryImpact;
            @XmlElement(name = "Counter", nillable = true)
            protected List<IODEFDocument.Incident.Assessment.Counter> counter;
            @XmlElement(name = "Confidence", nillable = true)
            protected List<IODEFDocument.Incident.Assessment.Confidence> confidence;
            @XmlElement(name = "AdditionalData", nillable = true)
            protected List<IODEFDocument.Incident.Assessment.AdditionalData> additionalData;
            @XmlAttribute(name = "occurrence")
            protected String occurrence;
            @XmlAttribute(name = "restriction")
            protected String restriction;

            /**
             * Gets the value of the impact property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the impact property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getImpact().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Assessment.Impact }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Assessment.Impact> getImpact() {
                if (impact == null) {
                    impact = new ArrayList<IODEFDocument.Incident.Assessment.Impact>();
                }
                return this.impact;
            }

            /**
             * Gets the value of the timeImpact property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the timeImpact property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getTimeImpact().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Assessment.TimeImpact }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Assessment.TimeImpact> getTimeImpact() {
                if (timeImpact == null) {
                    timeImpact = new ArrayList<IODEFDocument.Incident.Assessment.TimeImpact>();
                }
                return this.timeImpact;
            }

            /**
             * Gets the value of the monetaryImpact property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the monetaryImpact property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getMonetaryImpact().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Assessment.MonetaryImpact }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Assessment.MonetaryImpact> getMonetaryImpact() {
                if (monetaryImpact == null) {
                    monetaryImpact = new ArrayList<IODEFDocument.Incident.Assessment.MonetaryImpact>();
                }
                return this.monetaryImpact;
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
             * {@link IODEFDocument.Incident.Assessment.Counter }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Assessment.Counter> getCounter() {
                if (counter == null) {
                    counter = new ArrayList<IODEFDocument.Incident.Assessment.Counter>();
                }
                return this.counter;
            }

            /**
             * Gets the value of the confidence property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the confidence property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getConfidence().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Assessment.Confidence }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Assessment.Confidence> getConfidence() {
                if (confidence == null) {
                    confidence = new ArrayList<IODEFDocument.Incident.Assessment.Confidence>();
                }
                return this.confidence;
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
             * {@link IODEFDocument.Incident.Assessment.AdditionalData }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Assessment.AdditionalData> getAdditionalData() {
                if (additionalData == null) {
                    additionalData = new ArrayList<IODEFDocument.Incident.Assessment.AdditionalData>();
                }
                return this.additionalData;
            }

            /**
             * occurrenceプロパティの値を取得します。
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
             * occurrenceプロパティの値を設定します。
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
             * restrictionプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRestriction() {
                return restriction;
            }

            /**
             * restrictionプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRestriction(String value) {
                this.restriction = value;
            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class AdditionalData {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "dtype")
                protected String dtype;
                @XmlAttribute(name = "ext-dtype")
                protected String extDtype;
                @XmlAttribute(name = "meaning")
                protected String meaning;
                @XmlAttribute(name = "formatid")
                protected String formatid;
                @XmlAttribute(name = "restriction")
                protected String restriction;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * dtypeプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getDtype() {
                    return dtype;
                }

                /**
                 * dtypeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setDtype(String value) {
                    this.dtype = value;
                }

                /**
                 * extDtypeプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getExtDtype() {
                    return extDtype;
                }

                /**
                 * extDtypeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtDtype(String value) {
                    this.extDtype = value;
                }

                /**
                 * meaningプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getMeaning() {
                    return meaning;
                }

                /**
                 * meaningプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setMeaning(String value) {
                    this.meaning = value;
                }

                /**
                 * formatidプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getFormatid() {
                    return formatid;
                }

                /**
                 * formatidプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setFormatid(String value) {
                    this.formatid = value;
                }

                /**
                 * restrictionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getRestriction() {
                    return restriction;
                }

                /**
                 * restrictionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setRestriction(String value) {
                    this.restriction = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="rating" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class Confidence {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "rating")
                protected String rating;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * ratingプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getRating() {
                    return rating;
                }

                /**
                 * ratingプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setRating(String value) {
                    this.rating = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class Counter {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "type")
                protected String type;
                @XmlAttribute(name = "ext-type")
                protected String extType;
                @XmlAttribute(name = "meaning")
                protected String meaning;
                @XmlAttribute(name = "duration")
                protected String duration;
                @XmlAttribute(name = "ext-duration")
                protected String extDuration;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * typeプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getType() {
                    return type;
                }

                /**
                 * typeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setType(String value) {
                    this.type = value;
                }

                /**
                 * extTypeプロパティの値を取得します。
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
                 * extTypeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtType(String value) {
                    this.extType = value;
                }

                /**
                 * meaningプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getMeaning() {
                    return meaning;
                }

                /**
                 * meaningプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setMeaning(String value) {
                    this.meaning = value;
                }

                /**
                 * durationプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getDuration() {
                    return duration;
                }

                /**
                 * durationプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setDuration(String value) {
                    this.duration = value;
                }

                /**
                 * extDurationプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getExtDuration() {
                    return extDuration;
                }

                /**
                 * extDurationプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtDuration(String value) {
                    this.extDuration = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="completion" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class Impact {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "severity")
                protected String severity;
                @XmlAttribute(name = "completion")
                protected String completion;
                @XmlAttribute(name = "type")
                protected String type;
                @XmlAttribute(name = "ext-type")
                protected String extType;
                @XmlAttribute(name = "lang")
                protected String lang;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * severityプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getSeverity() {
                    return severity;
                }

                /**
                 * severityプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setSeverity(String value) {
                    this.severity = value;
                }

                /**
                 * completionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getCompletion() {
                    return completion;
                }

                /**
                 * completionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setCompletion(String value) {
                    this.completion = value;
                }

                /**
                 * typeプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getType() {
                    return type;
                }

                /**
                 * typeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setType(String value) {
                    this.type = value;
                }

                /**
                 * extTypeプロパティの値を取得します。
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
                 * extTypeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtType(String value) {
                    this.extType = value;
                }

                /**
                 * langプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getLang() {
                    return lang;
                }

                /**
                 * langプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setLang(String value) {
                    this.lang = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="currency" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class MonetaryImpact {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "severity")
                protected String severity;
                @XmlAttribute(name = "currency")
                protected String currency;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * severityプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getSeverity() {
                    return severity;
                }

                /**
                 * severityプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setSeverity(String value) {
                    this.severity = value;
                }

                /**
                 * currencyプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getCurrency() {
                    return currency;
                }

                /**
                 * currencyプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setCurrency(String value) {
                    this.currency = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="metric" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-metric" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="duration" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-duration" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class TimeImpact {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "severity")
                protected String severity;
                @XmlAttribute(name = "metric")
                protected String metric;
                @XmlAttribute(name = "ext-metric")
                protected String extMetric;
                @XmlAttribute(name = "duration")
                protected String duration;
                @XmlAttribute(name = "ext-duration")
                protected String extDuration;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * severityプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getSeverity() {
                    return severity;
                }

                /**
                 * severityプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setSeverity(String value) {
                    this.severity = value;
                }

                /**
                 * metricプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getMetric() {
                    return metric;
                }

                /**
                 * metricプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setMetric(String value) {
                    this.metric = value;
                }

                /**
                 * extMetricプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getExtMetric() {
                    return extMetric;
                }

                /**
                 * extMetricプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtMetric(String value) {
                    this.extMetric = value;
                }

                /**
                 * durationプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getDuration() {
                    return duration;
                }

                /**
                 * durationプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setDuration(String value) {
                    this.duration = value;
                }

                /**
                 * extDurationプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getExtDuration() {
                    return extDuration;
                }

                /**
                 * extDurationプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtDuration(String value) {
                    this.extDuration = value;
                }

            }

        }


        /**
         * <p>anonymous complex typeのJavaクラス。
         * 
         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;complexContent>
         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *       &lt;sequence>
         *         &lt;element name="Timezone" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *         &lt;element name="ContactName" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="RegistryHandle" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="registry" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-registry" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="PostalAddress" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="Email" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="Telephone" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="Fax" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;simpleContent>
         *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                 &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/extension>
         *             &lt;/simpleContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *       &lt;/sequence>
         *       &lt;attribute name="role" type="{http://www.w3.org/2001/XMLSchema}string" />
         *       &lt;attribute name="ext-role" type="{http://www.w3.org/2001/XMLSchema}string" />
         *       &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *       &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/restriction>
         *   &lt;/complexContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "", propOrder = {
            "timezone",
            "contactName",
            "registryHandle",
            "postalAddress",
            "email",
            "telephone",
            "fax"
        })
        public static class Contact {

            @XmlElement(name = "Timezone")
            protected String timezone;
            @XmlElement(name = "ContactName", nillable = true)
            protected List<IODEFDocument.Incident.Contact.ContactName> contactName;
            @XmlElement(name = "RegistryHandle", nillable = true)
            protected List<IODEFDocument.Incident.Contact.RegistryHandle> registryHandle;
            @XmlElement(name = "PostalAddress", nillable = true)
            protected List<IODEFDocument.Incident.Contact.PostalAddress> postalAddress;
            @XmlElement(name = "Email", nillable = true)
            protected List<IODEFDocument.Incident.Contact.Email> email;
            @XmlElement(name = "Telephone", nillable = true)
            protected List<IODEFDocument.Incident.Contact.Telephone> telephone;
            @XmlElement(name = "Fax", nillable = true)
            protected List<IODEFDocument.Incident.Contact.Fax> fax;
            @XmlAttribute(name = "role")
            protected String role;
            @XmlAttribute(name = "ext-role")
            protected String extRole;
            @XmlAttribute(name = "type")
            protected String type;
            @XmlAttribute(name = "ext-type")
            protected String extType;
            @XmlAttribute(name = "restriction")
            protected String restriction;

            /**
             * timezoneプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getTimezone() {
                return timezone;
            }

            /**
             * timezoneプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setTimezone(String value) {
                this.timezone = value;
            }

            /**
             * Gets the value of the contactName property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the contactName property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getContactName().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Contact.ContactName }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Contact.ContactName> getContactName() {
                if (contactName == null) {
                    contactName = new ArrayList<IODEFDocument.Incident.Contact.ContactName>();
                }
                return this.contactName;
            }

            /**
             * Gets the value of the registryHandle property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the registryHandle property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getRegistryHandle().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Contact.RegistryHandle }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Contact.RegistryHandle> getRegistryHandle() {
                if (registryHandle == null) {
                    registryHandle = new ArrayList<IODEFDocument.Incident.Contact.RegistryHandle>();
                }
                return this.registryHandle;
            }

            /**
             * Gets the value of the postalAddress property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the postalAddress property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getPostalAddress().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Contact.PostalAddress }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Contact.PostalAddress> getPostalAddress() {
                if (postalAddress == null) {
                    postalAddress = new ArrayList<IODEFDocument.Incident.Contact.PostalAddress>();
                }
                return this.postalAddress;
            }

            /**
             * Gets the value of the email property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the email property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getEmail().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Contact.Email }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Contact.Email> getEmail() {
                if (email == null) {
                    email = new ArrayList<IODEFDocument.Incident.Contact.Email>();
                }
                return this.email;
            }

            /**
             * Gets the value of the telephone property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the telephone property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getTelephone().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Contact.Telephone }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Contact.Telephone> getTelephone() {
                if (telephone == null) {
                    telephone = new ArrayList<IODEFDocument.Incident.Contact.Telephone>();
                }
                return this.telephone;
            }

            /**
             * Gets the value of the fax property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the fax property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getFax().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Contact.Fax }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Contact.Fax> getFax() {
                if (fax == null) {
                    fax = new ArrayList<IODEFDocument.Incident.Contact.Fax>();
                }
                return this.fax;
            }

            /**
             * roleプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRole() {
                return role;
            }

            /**
             * roleプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRole(String value) {
                this.role = value;
            }

            /**
             * extRoleプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getExtRole() {
                return extRole;
            }

            /**
             * extRoleプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setExtRole(String value) {
                this.extRole = value;
            }

            /**
             * typeプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getType() {
                return type;
            }

            /**
             * typeプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setType(String value) {
                this.type = value;
            }

            /**
             * extTypeプロパティの値を取得します。
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
             * extTypeプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setExtType(String value) {
                this.extType = value;
            }

            /**
             * restrictionプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRestriction() {
                return restriction;
            }

            /**
             * restrictionプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRestriction(String value) {
                this.restriction = value;
            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class ContactName {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "lang")
                protected String lang;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * langプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getLang() {
                    return lang;
                }

                /**
                 * langプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setLang(String value) {
                    this.lang = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class Email {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "meaning")
                protected String meaning;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * meaningプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getMeaning() {
                    return meaning;
                }

                /**
                 * meaningプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setMeaning(String value) {
                    this.meaning = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class Fax {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "meaning")
                protected String meaning;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * meaningプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getMeaning() {
                    return meaning;
                }

                /**
                 * meaningプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setMeaning(String value) {
                    this.meaning = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class PostalAddress {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "meaning")
                protected String meaning;
                @XmlAttribute(name = "lang")
                protected String lang;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * meaningプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getMeaning() {
                    return meaning;
                }

                /**
                 * meaningプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setMeaning(String value) {
                    this.meaning = value;
                }

                /**
                 * langプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getLang() {
                    return lang;
                }

                /**
                 * langプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setLang(String value) {
                    this.lang = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="registry" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-registry" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class RegistryHandle {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "registry")
                protected String registry;
                @XmlAttribute(name = "ext-registry")
                protected String extRegistry;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * registryプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getRegistry() {
                    return registry;
                }

                /**
                 * registryプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setRegistry(String value) {
                    this.registry = value;
                }

                /**
                 * extRegistryプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getExtRegistry() {
                    return extRegistry;
                }

                /**
                 * extRegistryプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtRegistry(String value) {
                    this.extRegistry = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;simpleContent>
             *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *       &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/extension>
             *   &lt;/simpleContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "value"
            })
            public static class Telephone {

                @XmlValue
                protected String value;
                @XmlAttribute(name = "meaning")
                protected String meaning;

                /**
                 * valueプロパティの値を取得します。
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
                 * valueプロパティの値を設定します。
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
                 * meaningプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getMeaning() {
                    return meaning;
                }

                /**
                 * meaningプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setMeaning(String value) {
                    this.meaning = value;
                }

            }

        }


        /**
         * <p>anonymous complex typeのJavaクラス。
         * 
         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;complexContent>
         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *       &lt;sequence>
         *         &lt;element name="DetectTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *         &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *         &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *         &lt;element name="Flow" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;complexContent>
         *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                 &lt;sequence>
         *                   &lt;element name="System" maxOccurs="unbounded" minOccurs="0">
         *                     &lt;complexType>
         *                       &lt;complexContent>
         *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                           &lt;sequence>
         *                             &lt;element name="Node" maxOccurs="unbounded" minOccurs="0">
         *                               &lt;complexType>
         *                                 &lt;complexContent>
         *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                                     &lt;sequence>
         *                                       &lt;element name="Counter" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                       &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                       &lt;element name="NodeName" maxOccurs="unbounded" minOccurs="0">
         *                                         &lt;complexType>
         *                                           &lt;simpleContent>
         *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                                               &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                             &lt;/extension>
         *                                           &lt;/simpleContent>
         *                                         &lt;/complexType>
         *                                       &lt;/element>
         *                                       &lt;element name="Address" maxOccurs="unbounded" minOccurs="0">
         *                                         &lt;complexType>
         *                                           &lt;simpleContent>
         *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                                               &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="vlan-name" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="vlan-num" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                             &lt;/extension>
         *                                           &lt;/simpleContent>
         *                                         &lt;/complexType>
         *                                       &lt;/element>
         *                                       &lt;element name="Location" maxOccurs="unbounded" minOccurs="0">
         *                                         &lt;complexType>
         *                                           &lt;simpleContent>
         *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                                               &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                             &lt;/extension>
         *                                           &lt;/simpleContent>
         *                                         &lt;/complexType>
         *                                       &lt;/element>
         *                                       &lt;element name="NodeRole" maxOccurs="unbounded" minOccurs="0">
         *                                         &lt;complexType>
         *                                           &lt;simpleContent>
         *                                             &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                                               &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                             &lt;/extension>
         *                                           &lt;/simpleContent>
         *                                         &lt;/complexType>
         *                                       &lt;/element>
         *                                     &lt;/sequence>
         *                                   &lt;/restriction>
         *                                 &lt;/complexContent>
         *                               &lt;/complexType>
         *                             &lt;/element>
         *                             &lt;element name="Service" maxOccurs="unbounded" minOccurs="0">
         *                               &lt;complexType>
         *                                 &lt;complexContent>
         *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                                     &lt;sequence>
         *                                       &lt;element name="Port" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                       &lt;element name="Portlist" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                       &lt;element name="ProtoType" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                       &lt;element name="ProtoCode" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                       &lt;element name="ProtoField" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                       &lt;element name="Application" maxOccurs="unbounded" minOccurs="0">
         *                                         &lt;complexType>
         *                                           &lt;complexContent>
         *                                             &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                                               &lt;sequence>
         *                                                 &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                               &lt;/sequence>
         *                                               &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                               &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                             &lt;/restriction>
         *                                           &lt;/complexContent>
         *                                         &lt;/complexType>
         *                                       &lt;/element>
         *                                     &lt;/sequence>
         *                                     &lt;attribute name="ip_protocol" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                   &lt;/restriction>
         *                                 &lt;/complexContent>
         *                               &lt;/complexType>
         *                             &lt;/element>
         *                             &lt;element name="OperatingSystem" maxOccurs="unbounded" minOccurs="0">
         *                               &lt;complexType>
         *                                 &lt;complexContent>
         *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                                     &lt;sequence>
         *                                       &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                                     &lt;/sequence>
         *                                     &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                   &lt;/restriction>
         *                                 &lt;/complexContent>
         *                               &lt;/complexType>
         *                             &lt;/element>
         *                           &lt;/sequence>
         *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                           &lt;attribute name="interface" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                           &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                           &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                           &lt;attribute name="spoofed" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                         &lt;/restriction>
         *                       &lt;/complexContent>
         *                     &lt;/complexType>
         *                   &lt;/element>
         *                 &lt;/sequence>
         *               &lt;/restriction>
         *             &lt;/complexContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="Expectation" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;complexContent>
         *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                 &lt;sequence>
         *                   &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                   &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                 &lt;/sequence>
         *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/restriction>
         *             &lt;/complexContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element name="Record" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;complexContent>
         *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                 &lt;sequence>
         *                   &lt;element name="RecordData" maxOccurs="unbounded" minOccurs="0">
         *                     &lt;complexType>
         *                       &lt;complexContent>
         *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                           &lt;sequence>
         *                             &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                             &lt;element name="RecordPattern" maxOccurs="unbounded" minOccurs="0">
         *                               &lt;complexType>
         *                                 &lt;simpleContent>
         *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                                     &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="offset" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="ext-offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="instance" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                   &lt;/extension>
         *                                 &lt;/simpleContent>
         *                               &lt;/complexType>
         *                             &lt;/element>
         *                             &lt;element name="RecordItem" maxOccurs="unbounded" minOccurs="0">
         *                               &lt;complexType>
         *                                 &lt;simpleContent>
         *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                                     &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                     &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                                   &lt;/extension>
         *                                 &lt;/simpleContent>
         *                               &lt;/complexType>
         *                             &lt;/element>
         *                           &lt;/sequence>
         *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                         &lt;/restriction>
         *                       &lt;/complexContent>
         *                     &lt;/complexType>
         *                   &lt;/element>
         *                 &lt;/sequence>
         *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/restriction>
         *             &lt;/complexContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *       &lt;/sequence>
         *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/restriction>
         *   &lt;/complexContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "", propOrder = {
            "detectTime",
            "startTime",
            "endTime",
            "flow",
            "expectation",
            "record"
        })
        public static class EventData {

            @XmlElement(name = "DetectTime")
            protected String detectTime;
            @XmlElement(name = "StartTime")
            protected String startTime;
            @XmlElement(name = "EndTime")
            protected String endTime;
            @XmlElement(name = "Flow")
            protected List<IODEFDocument.Incident.EventData.Flow> flow;
            @XmlElement(name = "Expectation")
            protected List<IODEFDocument.Incident.EventData.Expectation> expectation;
            @XmlElement(name = "Record")
            protected List<IODEFDocument.Incident.EventData.Record> record;
            @XmlAttribute(name = "restriction")
            protected String restriction;

            /**
             * detectTimeプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getDetectTime() {
                return detectTime;
            }

            /**
             * detectTimeプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setDetectTime(String value) {
                this.detectTime = value;
            }

            /**
             * startTimeプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getStartTime() {
                return startTime;
            }

            /**
             * startTimeプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setStartTime(String value) {
                this.startTime = value;
            }

            /**
             * endTimeプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getEndTime() {
                return endTime;
            }

            /**
             * endTimeプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setEndTime(String value) {
                this.endTime = value;
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
             * {@link IODEFDocument.Incident.EventData.Flow }
             * 
             * 
             */
            public List<IODEFDocument.Incident.EventData.Flow> getFlow() {
                if (flow == null) {
                    flow = new ArrayList<IODEFDocument.Incident.EventData.Flow>();
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
             * {@link IODEFDocument.Incident.EventData.Expectation }
             * 
             * 
             */
            public List<IODEFDocument.Incident.EventData.Expectation> getExpectation() {
                if (expectation == null) {
                    expectation = new ArrayList<IODEFDocument.Incident.EventData.Expectation>();
                }
                return this.expectation;
            }

            /**
             * Gets the value of the record property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the record property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getRecord().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.EventData.Record }
             * 
             * 
             */
            public List<IODEFDocument.Incident.EventData.Record> getRecord() {
                if (record == null) {
                    record = new ArrayList<IODEFDocument.Incident.EventData.Record>();
                }
                return this.record;
            }

            /**
             * restrictionプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRestriction() {
                return restriction;
            }

            /**
             * restrictionプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRestriction(String value) {
                this.restriction = value;
            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;complexContent>
             *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *       &lt;sequence>
             *         &lt;element name="StartTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *         &lt;element name="EndTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *       &lt;/sequence>
             *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="severity" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/restriction>
             *   &lt;/complexContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "startTime",
                "endTime"
            })
            public static class Expectation {

                @XmlElement(name = "StartTime")
                protected String startTime;
                @XmlElement(name = "EndTime")
                protected String endTime;
                @XmlAttribute(name = "restriction")
                protected String restriction;
                @XmlAttribute(name = "severity")
                protected String severity;
                @XmlAttribute(name = "action")
                protected String action;
                @XmlAttribute(name = "ext-action")
                protected String extAction;

                /**
                 * startTimeプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getStartTime() {
                    return startTime;
                }

                /**
                 * startTimeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setStartTime(String value) {
                    this.startTime = value;
                }

                /**
                 * endTimeプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getEndTime() {
                    return endTime;
                }

                /**
                 * endTimeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setEndTime(String value) {
                    this.endTime = value;
                }

                /**
                 * restrictionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getRestriction() {
                    return restriction;
                }

                /**
                 * restrictionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setRestriction(String value) {
                    this.restriction = value;
                }

                /**
                 * severityプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getSeverity() {
                    return severity;
                }

                /**
                 * severityプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setSeverity(String value) {
                    this.severity = value;
                }

                /**
                 * actionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getAction() {
                    return action;
                }

                /**
                 * actionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setAction(String value) {
                    this.action = value;
                }

                /**
                 * extActionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getExtAction() {
                    return extAction;
                }

                /**
                 * extActionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtAction(String value) {
                    this.extAction = value;
                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;complexContent>
             *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *       &lt;sequence>
             *         &lt;element name="System" maxOccurs="unbounded" minOccurs="0">
             *           &lt;complexType>
             *             &lt;complexContent>
             *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *                 &lt;sequence>
             *                   &lt;element name="Node" maxOccurs="unbounded" minOccurs="0">
             *                     &lt;complexType>
             *                       &lt;complexContent>
             *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *                           &lt;sequence>
             *                             &lt;element name="Counter" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                             &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                             &lt;element name="NodeName" maxOccurs="unbounded" minOccurs="0">
             *                               &lt;complexType>
             *                                 &lt;simpleContent>
             *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *                                     &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                   &lt;/extension>
             *                                 &lt;/simpleContent>
             *                               &lt;/complexType>
             *                             &lt;/element>
             *                             &lt;element name="Address" maxOccurs="unbounded" minOccurs="0">
             *                               &lt;complexType>
             *                                 &lt;simpleContent>
             *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *                                     &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="vlan-name" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="vlan-num" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                   &lt;/extension>
             *                                 &lt;/simpleContent>
             *                               &lt;/complexType>
             *                             &lt;/element>
             *                             &lt;element name="Location" maxOccurs="unbounded" minOccurs="0">
             *                               &lt;complexType>
             *                                 &lt;simpleContent>
             *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *                                     &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                   &lt;/extension>
             *                                 &lt;/simpleContent>
             *                               &lt;/complexType>
             *                             &lt;/element>
             *                             &lt;element name="NodeRole" maxOccurs="unbounded" minOccurs="0">
             *                               &lt;complexType>
             *                                 &lt;simpleContent>
             *                                   &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *                                     &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                   &lt;/extension>
             *                                 &lt;/simpleContent>
             *                               &lt;/complexType>
             *                             &lt;/element>
             *                           &lt;/sequence>
             *                         &lt;/restriction>
             *                       &lt;/complexContent>
             *                     &lt;/complexType>
             *                   &lt;/element>
             *                   &lt;element name="Service" maxOccurs="unbounded" minOccurs="0">
             *                     &lt;complexType>
             *                       &lt;complexContent>
             *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *                           &lt;sequence>
             *                             &lt;element name="Port" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                             &lt;element name="Portlist" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                             &lt;element name="ProtoType" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                             &lt;element name="ProtoCode" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                             &lt;element name="ProtoField" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                             &lt;element name="Application" maxOccurs="unbounded" minOccurs="0">
             *                               &lt;complexType>
             *                                 &lt;complexContent>
             *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *                                     &lt;sequence>
             *                                       &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                                     &lt;/sequence>
             *                                     &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                     &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                                   &lt;/restriction>
             *                                 &lt;/complexContent>
             *                               &lt;/complexType>
             *                             &lt;/element>
             *                           &lt;/sequence>
             *                           &lt;attribute name="ip_protocol" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                         &lt;/restriction>
             *                       &lt;/complexContent>
             *                     &lt;/complexType>
             *                   &lt;/element>
             *                   &lt;element name="OperatingSystem" maxOccurs="unbounded" minOccurs="0">
             *                     &lt;complexType>
             *                       &lt;complexContent>
             *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *                           &lt;sequence>
             *                             &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                           &lt;/sequence>
             *                           &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                         &lt;/restriction>
             *                       &lt;/complexContent>
             *                     &lt;/complexType>
             *                   &lt;/element>
             *                 &lt;/sequence>
             *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                 &lt;attribute name="interface" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                 &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                 &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                 &lt;attribute name="spoofed" type="{http://www.w3.org/2001/XMLSchema}string" />
             *               &lt;/restriction>
             *             &lt;/complexContent>
             *           &lt;/complexType>
             *         &lt;/element>
             *       &lt;/sequence>
             *     &lt;/restriction>
             *   &lt;/complexContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "system"
            })
            public static class Flow {

                @XmlElement(name = "System")
                protected List<IODEFDocument.Incident.EventData.Flow.System> system;

                /**
                 * Gets the value of the system property.
                 * 
                 * <p>
                 * This accessor method returns a reference to the live list,
                 * not a snapshot. Therefore any modification you make to the
                 * returned list will be present inside the JAXB object.
                 * This is why there is not a <CODE>set</CODE> method for the system property.
                 * 
                 * <p>
                 * For example, to add a new item, do as follows:
                 * <pre>
                 *    getSystem().add(newItem);
                 * </pre>
                 * 
                 * 
                 * <p>
                 * Objects of the following type(s) are allowed in the list
                 * {@link IODEFDocument.Incident.EventData.Flow.System }
                 * 
                 * 
                 */
                public List<IODEFDocument.Incident.EventData.Flow.System> getSystem() {
                    if (system == null) {
                        system = new ArrayList<IODEFDocument.Incident.EventData.Flow.System>();
                    }
                    return this.system;
                }


                /**
                 * <p>anonymous complex typeのJavaクラス。
                 * 
                 * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                 * 
                 * <pre>
                 * &lt;complexType>
                 *   &lt;complexContent>
                 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                 *       &lt;sequence>
                 *         &lt;element name="Node" maxOccurs="unbounded" minOccurs="0">
                 *           &lt;complexType>
                 *             &lt;complexContent>
                 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                 *                 &lt;sequence>
                 *                   &lt;element name="Counter" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                   &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                   &lt;element name="NodeName" maxOccurs="unbounded" minOccurs="0">
                 *                     &lt;complexType>
                 *                       &lt;simpleContent>
                 *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *                           &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                         &lt;/extension>
                 *                       &lt;/simpleContent>
                 *                     &lt;/complexType>
                 *                   &lt;/element>
                 *                   &lt;element name="Address" maxOccurs="unbounded" minOccurs="0">
                 *                     &lt;complexType>
                 *                       &lt;simpleContent>
                 *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *                           &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="vlan-name" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="vlan-num" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                         &lt;/extension>
                 *                       &lt;/simpleContent>
                 *                     &lt;/complexType>
                 *                   &lt;/element>
                 *                   &lt;element name="Location" maxOccurs="unbounded" minOccurs="0">
                 *                     &lt;complexType>
                 *                       &lt;simpleContent>
                 *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *                           &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                         &lt;/extension>
                 *                       &lt;/simpleContent>
                 *                     &lt;/complexType>
                 *                   &lt;/element>
                 *                   &lt;element name="NodeRole" maxOccurs="unbounded" minOccurs="0">
                 *                     &lt;complexType>
                 *                       &lt;simpleContent>
                 *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *                           &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                         &lt;/extension>
                 *                       &lt;/simpleContent>
                 *                     &lt;/complexType>
                 *                   &lt;/element>
                 *                 &lt;/sequence>
                 *               &lt;/restriction>
                 *             &lt;/complexContent>
                 *           &lt;/complexType>
                 *         &lt;/element>
                 *         &lt;element name="Service" maxOccurs="unbounded" minOccurs="0">
                 *           &lt;complexType>
                 *             &lt;complexContent>
                 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                 *                 &lt;sequence>
                 *                   &lt;element name="Port" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                   &lt;element name="Portlist" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                   &lt;element name="ProtoType" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                   &lt;element name="ProtoCode" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                   &lt;element name="ProtoField" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                   &lt;element name="Application" maxOccurs="unbounded" minOccurs="0">
                 *                     &lt;complexType>
                 *                       &lt;complexContent>
                 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                 *                           &lt;sequence>
                 *                             &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                           &lt;/sequence>
                 *                           &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                           &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                         &lt;/restriction>
                 *                       &lt;/complexContent>
                 *                     &lt;/complexType>
                 *                   &lt;/element>
                 *                 &lt;/sequence>
                 *                 &lt;attribute name="ip_protocol" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *               &lt;/restriction>
                 *             &lt;/complexContent>
                 *           &lt;/complexType>
                 *         &lt;/element>
                 *         &lt;element name="OperatingSystem" maxOccurs="unbounded" minOccurs="0">
                 *           &lt;complexType>
                 *             &lt;complexContent>
                 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                 *                 &lt;sequence>
                 *                   &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *                 &lt;/sequence>
                 *                 &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *               &lt;/restriction>
                 *             &lt;/complexContent>
                 *           &lt;/complexType>
                 *         &lt;/element>
                 *       &lt;/sequence>
                 *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *       &lt;attribute name="interface" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *       &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *       &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *       &lt;attribute name="spoofed" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *     &lt;/restriction>
                 *   &lt;/complexContent>
                 * &lt;/complexType>
                 * </pre>
                 * 
                 * 
                 */
                @XmlAccessorType(XmlAccessType.FIELD)
                @XmlType(name = "", propOrder = {
                    "node",
                    "service",
                    "operatingSystem"
                })
                public static class System {

                    @XmlElement(name = "Node")
                    protected List<IODEFDocument.Incident.EventData.Flow.System.Node> node;
                    @XmlElement(name = "Service")
                    protected List<IODEFDocument.Incident.EventData.Flow.System.Service> service;
                    @XmlElement(name = "OperatingSystem")
                    protected List<IODEFDocument.Incident.EventData.Flow.System.OperatingSystem> operatingSystem;
                    @XmlAttribute(name = "restriction")
                    protected String restriction;
                    @XmlAttribute(name = "interface")
                    protected String _interface;
                    @XmlAttribute(name = "category")
                    protected String category;
                    @XmlAttribute(name = "ext-category")
                    protected String extCategory;
                    @XmlAttribute(name = "spoofed")
                    protected String spoofed;

                    /**
                     * Gets the value of the node property.
                     * 
                     * <p>
                     * This accessor method returns a reference to the live list,
                     * not a snapshot. Therefore any modification you make to the
                     * returned list will be present inside the JAXB object.
                     * This is why there is not a <CODE>set</CODE> method for the node property.
                     * 
                     * <p>
                     * For example, to add a new item, do as follows:
                     * <pre>
                     *    getNode().add(newItem);
                     * </pre>
                     * 
                     * 
                     * <p>
                     * Objects of the following type(s) are allowed in the list
                     * {@link IODEFDocument.Incident.EventData.Flow.System.Node }
                     * 
                     * 
                     */
                    public List<IODEFDocument.Incident.EventData.Flow.System.Node> getNode() {
                        if (node == null) {
                            node = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.Node>();
                        }
                        return this.node;
                    }

                    /**
                     * Gets the value of the service property.
                     * 
                     * <p>
                     * This accessor method returns a reference to the live list,
                     * not a snapshot. Therefore any modification you make to the
                     * returned list will be present inside the JAXB object.
                     * This is why there is not a <CODE>set</CODE> method for the service property.
                     * 
                     * <p>
                     * For example, to add a new item, do as follows:
                     * <pre>
                     *    getService().add(newItem);
                     * </pre>
                     * 
                     * 
                     * <p>
                     * Objects of the following type(s) are allowed in the list
                     * {@link IODEFDocument.Incident.EventData.Flow.System.Service }
                     * 
                     * 
                     */
                    public List<IODEFDocument.Incident.EventData.Flow.System.Service> getService() {
                        if (service == null) {
                            service = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.Service>();
                        }
                        return this.service;
                    }

                    /**
                     * Gets the value of the operatingSystem property.
                     * 
                     * <p>
                     * This accessor method returns a reference to the live list,
                     * not a snapshot. Therefore any modification you make to the
                     * returned list will be present inside the JAXB object.
                     * This is why there is not a <CODE>set</CODE> method for the operatingSystem property.
                     * 
                     * <p>
                     * For example, to add a new item, do as follows:
                     * <pre>
                     *    getOperatingSystem().add(newItem);
                     * </pre>
                     * 
                     * 
                     * <p>
                     * Objects of the following type(s) are allowed in the list
                     * {@link IODEFDocument.Incident.EventData.Flow.System.OperatingSystem }
                     * 
                     * 
                     */
                    public List<IODEFDocument.Incident.EventData.Flow.System.OperatingSystem> getOperatingSystem() {
                        if (operatingSystem == null) {
                            operatingSystem = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.OperatingSystem>();
                        }
                        return this.operatingSystem;
                    }

                    /**
                     * restrictionプロパティの値を取得します。
                     * 
                     * @return
                     *     possible object is
                     *     {@link String }
                     *     
                     */
                    public String getRestriction() {
                        return restriction;
                    }

                    /**
                     * restrictionプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setRestriction(String value) {
                        this.restriction = value;
                    }

                    /**
                     * interfaceプロパティの値を取得します。
                     * 
                     * @return
                     *     possible object is
                     *     {@link String }
                     *     
                     */
                    public String getInterface() {
                        return _interface;
                    }

                    /**
                     * interfaceプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setInterface(String value) {
                        this._interface = value;
                    }

                    /**
                     * categoryプロパティの値を取得します。
                     * 
                     * @return
                     *     possible object is
                     *     {@link String }
                     *     
                     */
                    public String getCategory() {
                        return category;
                    }

                    /**
                     * categoryプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setCategory(String value) {
                        this.category = value;
                    }

                    /**
                     * extCategoryプロパティの値を取得します。
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
                     * extCategoryプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setExtCategory(String value) {
                        this.extCategory = value;
                    }

                    /**
                     * spoofedプロパティの値を取得します。
                     * 
                     * @return
                     *     possible object is
                     *     {@link String }
                     *     
                     */
                    public String getSpoofed() {
                        return spoofed;
                    }

                    /**
                     * spoofedプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setSpoofed(String value) {
                        this.spoofed = value;
                    }


                    /**
                     * <p>anonymous complex typeのJavaクラス。
                     * 
                     * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                     * 
                     * <pre>
                     * &lt;complexType>
                     *   &lt;complexContent>
                     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                     *       &lt;sequence>
                     *         &lt;element name="Counter" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *         &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *         &lt;element name="NodeName" maxOccurs="unbounded" minOccurs="0">
                     *           &lt;complexType>
                     *             &lt;simpleContent>
                     *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                     *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *               &lt;/extension>
                     *             &lt;/simpleContent>
                     *           &lt;/complexType>
                     *         &lt;/element>
                     *         &lt;element name="Address" maxOccurs="unbounded" minOccurs="0">
                     *           &lt;complexType>
                     *             &lt;simpleContent>
                     *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                     *                 &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="vlan-name" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="vlan-num" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *               &lt;/extension>
                     *             &lt;/simpleContent>
                     *           &lt;/complexType>
                     *         &lt;/element>
                     *         &lt;element name="Location" maxOccurs="unbounded" minOccurs="0">
                     *           &lt;complexType>
                     *             &lt;simpleContent>
                     *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                     *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *               &lt;/extension>
                     *             &lt;/simpleContent>
                     *           &lt;/complexType>
                     *         &lt;/element>
                     *         &lt;element name="NodeRole" maxOccurs="unbounded" minOccurs="0">
                     *           &lt;complexType>
                     *             &lt;simpleContent>
                     *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                     *                 &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *               &lt;/extension>
                     *             &lt;/simpleContent>
                     *           &lt;/complexType>
                     *         &lt;/element>
                     *       &lt;/sequence>
                     *     &lt;/restriction>
                     *   &lt;/complexContent>
                     * &lt;/complexType>
                     * </pre>
                     * 
                     * 
                     */
                    @XmlAccessorType(XmlAccessType.FIELD)
                    @XmlType(name = "", propOrder = {
                        "counter",
                        "dateTime",
                        "nodeName",
                        "address",
                        "location",
                        "nodeRole"
                    })
                    public static class Node {

                        @XmlElement(name = "Counter")
                        protected String counter;
                        @XmlElement(name = "DateTime")
                        protected String dateTime;
                        @XmlElement(name = "NodeName", nillable = true)
                        protected List<IODEFDocument.Incident.EventData.Flow.System.Node.NodeName> nodeName;
                        @XmlElement(name = "Address", nillable = true)
                        protected List<IODEFDocument.Incident.EventData.Flow.System.Node.Address> address;
                        @XmlElement(name = "Location", nillable = true)
                        protected List<IODEFDocument.Incident.EventData.Flow.System.Node.Location> location;
                        @XmlElement(name = "NodeRole", nillable = true)
                        protected List<IODEFDocument.Incident.EventData.Flow.System.Node.NodeRole> nodeRole;

                        /**
                         * counterプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getCounter() {
                            return counter;
                        }

                        /**
                         * counterプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setCounter(String value) {
                            this.counter = value;
                        }

                        /**
                         * dateTimeプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getDateTime() {
                            return dateTime;
                        }

                        /**
                         * dateTimeプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setDateTime(String value) {
                            this.dateTime = value;
                        }

                        /**
                         * Gets the value of the nodeName property.
                         * 
                         * <p>
                         * This accessor method returns a reference to the live list,
                         * not a snapshot. Therefore any modification you make to the
                         * returned list will be present inside the JAXB object.
                         * This is why there is not a <CODE>set</CODE> method for the nodeName property.
                         * 
                         * <p>
                         * For example, to add a new item, do as follows:
                         * <pre>
                         *    getNodeName().add(newItem);
                         * </pre>
                         * 
                         * 
                         * <p>
                         * Objects of the following type(s) are allowed in the list
                         * {@link IODEFDocument.Incident.EventData.Flow.System.Node.NodeName }
                         * 
                         * 
                         */
                        public List<IODEFDocument.Incident.EventData.Flow.System.Node.NodeName> getNodeName() {
                            if (nodeName == null) {
                                nodeName = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.Node.NodeName>();
                            }
                            return this.nodeName;
                        }

                        /**
                         * Gets the value of the address property.
                         * 
                         * <p>
                         * This accessor method returns a reference to the live list,
                         * not a snapshot. Therefore any modification you make to the
                         * returned list will be present inside the JAXB object.
                         * This is why there is not a <CODE>set</CODE> method for the address property.
                         * 
                         * <p>
                         * For example, to add a new item, do as follows:
                         * <pre>
                         *    getAddress().add(newItem);
                         * </pre>
                         * 
                         * 
                         * <p>
                         * Objects of the following type(s) are allowed in the list
                         * {@link IODEFDocument.Incident.EventData.Flow.System.Node.Address }
                         * 
                         * 
                         */
                        public List<IODEFDocument.Incident.EventData.Flow.System.Node.Address> getAddress() {
                            if (address == null) {
                                address = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.Node.Address>();
                            }
                            return this.address;
                        }

                        /**
                         * Gets the value of the location property.
                         * 
                         * <p>
                         * This accessor method returns a reference to the live list,
                         * not a snapshot. Therefore any modification you make to the
                         * returned list will be present inside the JAXB object.
                         * This is why there is not a <CODE>set</CODE> method for the location property.
                         * 
                         * <p>
                         * For example, to add a new item, do as follows:
                         * <pre>
                         *    getLocation().add(newItem);
                         * </pre>
                         * 
                         * 
                         * <p>
                         * Objects of the following type(s) are allowed in the list
                         * {@link IODEFDocument.Incident.EventData.Flow.System.Node.Location }
                         * 
                         * 
                         */
                        public List<IODEFDocument.Incident.EventData.Flow.System.Node.Location> getLocation() {
                            if (location == null) {
                                location = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.Node.Location>();
                            }
                            return this.location;
                        }

                        /**
                         * Gets the value of the nodeRole property.
                         * 
                         * <p>
                         * This accessor method returns a reference to the live list,
                         * not a snapshot. Therefore any modification you make to the
                         * returned list will be present inside the JAXB object.
                         * This is why there is not a <CODE>set</CODE> method for the nodeRole property.
                         * 
                         * <p>
                         * For example, to add a new item, do as follows:
                         * <pre>
                         *    getNodeRole().add(newItem);
                         * </pre>
                         * 
                         * 
                         * <p>
                         * Objects of the following type(s) are allowed in the list
                         * {@link IODEFDocument.Incident.EventData.Flow.System.Node.NodeRole }
                         * 
                         * 
                         */
                        public List<IODEFDocument.Incident.EventData.Flow.System.Node.NodeRole> getNodeRole() {
                            if (nodeRole == null) {
                                nodeRole = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.Node.NodeRole>();
                            }
                            return this.nodeRole;
                        }


                        /**
                         * <p>anonymous complex typeのJavaクラス。
                         * 
                         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                         * 
                         * <pre>
                         * &lt;complexType>
                         *   &lt;simpleContent>
                         *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                         *       &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="vlan-name" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="vlan-num" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *     &lt;/extension>
                         *   &lt;/simpleContent>
                         * &lt;/complexType>
                         * </pre>
                         * 
                         * 
                         */
                        @XmlAccessorType(XmlAccessType.FIELD)
                        @XmlType(name = "", propOrder = {
                            "value"
                        })
                        public static class Address {

                            @XmlValue
                            protected String value;
                            @XmlAttribute(name = "category")
                            protected String category;
                            @XmlAttribute(name = "ext-category")
                            protected String extCategory;
                            @XmlAttribute(name = "vlan-name")
                            protected String vlanName;
                            @XmlAttribute(name = "vlan-num")
                            protected String vlanNum;

                            /**
                             * valueプロパティの値を取得します。
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
                             * valueプロパティの値を設定します。
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
                             * categoryプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getCategory() {
                                return category;
                            }

                            /**
                             * categoryプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setCategory(String value) {
                                this.category = value;
                            }

                            /**
                             * extCategoryプロパティの値を取得します。
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
                             * extCategoryプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setExtCategory(String value) {
                                this.extCategory = value;
                            }

                            /**
                             * vlanNameプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getVlanName() {
                                return vlanName;
                            }

                            /**
                             * vlanNameプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setVlanName(String value) {
                                this.vlanName = value;
                            }

                            /**
                             * vlanNumプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getVlanNum() {
                                return vlanNum;
                            }

                            /**
                             * vlanNumプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setVlanNum(String value) {
                                this.vlanNum = value;
                            }

                        }


                        /**
                         * <p>anonymous complex typeのJavaクラス。
                         * 
                         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                         * 
                         * <pre>
                         * &lt;complexType>
                         *   &lt;simpleContent>
                         *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                         *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *     &lt;/extension>
                         *   &lt;/simpleContent>
                         * &lt;/complexType>
                         * </pre>
                         * 
                         * 
                         */
                        @XmlAccessorType(XmlAccessType.FIELD)
                        @XmlType(name = "", propOrder = {
                            "value"
                        })
                        public static class Location {

                            @XmlValue
                            protected String value;
                            @XmlAttribute(name = "lang")
                            protected String lang;

                            /**
                             * valueプロパティの値を取得します。
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
                             * valueプロパティの値を設定します。
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
                             * langプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getLang() {
                                return lang;
                            }

                            /**
                             * langプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setLang(String value) {
                                this.lang = value;
                            }

                        }


                        /**
                         * <p>anonymous complex typeのJavaクラス。
                         * 
                         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                         * 
                         * <pre>
                         * &lt;complexType>
                         *   &lt;simpleContent>
                         *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                         *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *     &lt;/extension>
                         *   &lt;/simpleContent>
                         * &lt;/complexType>
                         * </pre>
                         * 
                         * 
                         */
                        @XmlAccessorType(XmlAccessType.FIELD)
                        @XmlType(name = "", propOrder = {
                            "value"
                        })
                        public static class NodeName {

                            @XmlValue
                            protected String value;
                            @XmlAttribute(name = "lang")
                            protected String lang;

                            /**
                             * valueプロパティの値を取得します。
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
                             * valueプロパティの値を設定します。
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
                             * langプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getLang() {
                                return lang;
                            }

                            /**
                             * langプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setLang(String value) {
                                this.lang = value;
                            }

                        }


                        /**
                         * <p>anonymous complex typeのJavaクラス。
                         * 
                         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                         * 
                         * <pre>
                         * &lt;complexType>
                         *   &lt;simpleContent>
                         *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                         *       &lt;attribute name="category" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="ext-category" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *     &lt;/extension>
                         *   &lt;/simpleContent>
                         * &lt;/complexType>
                         * </pre>
                         * 
                         * 
                         */
                        @XmlAccessorType(XmlAccessType.FIELD)
                        @XmlType(name = "", propOrder = {
                            "value"
                        })
                        public static class NodeRole {

                            @XmlValue
                            protected String value;
                            @XmlAttribute(name = "category")
                            protected String category;
                            @XmlAttribute(name = "ext-category")
                            protected String extCategory;
                            @XmlAttribute(name = "lang")
                            protected String lang;

                            /**
                             * valueプロパティの値を取得します。
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
                             * valueプロパティの値を設定します。
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
                             * categoryプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getCategory() {
                                return category;
                            }

                            /**
                             * categoryプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setCategory(String value) {
                                this.category = value;
                            }

                            /**
                             * extCategoryプロパティの値を取得します。
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
                             * extCategoryプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setExtCategory(String value) {
                                this.extCategory = value;
                            }

                            /**
                             * langプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getLang() {
                                return lang;
                            }

                            /**
                             * langプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setLang(String value) {
                                this.lang = value;
                            }

                        }

                    }


                    /**
                     * <p>anonymous complex typeのJavaクラス。
                     * 
                     * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                     * 
                     * <pre>
                     * &lt;complexType>
                     *   &lt;complexContent>
                     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                     *       &lt;sequence>
                     *         &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *       &lt;/sequence>
                     *       &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *     &lt;/restriction>
                     *   &lt;/complexContent>
                     * &lt;/complexType>
                     * </pre>
                     * 
                     * 
                     */
                    @XmlAccessorType(XmlAccessType.FIELD)
                    @XmlType(name = "", propOrder = {
                        "url"
                    })
                    public static class OperatingSystem {

                        @XmlElement(name = "URL")
                        protected String url;
                        @XmlAttribute(name = "swid")
                        protected String swid;
                        @XmlAttribute(name = "configid")
                        protected String configid;
                        @XmlAttribute(name = "vendor")
                        protected String vendor;
                        @XmlAttribute(name = "family")
                        protected String family;
                        @XmlAttribute(name = "name")
                        protected String name;
                        @XmlAttribute(name = "version")
                        protected String version;
                        @XmlAttribute(name = "patch")
                        protected String patch;

                        /**
                         * urlプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getURL() {
                            return url;
                        }

                        /**
                         * urlプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setURL(String value) {
                            this.url = value;
                        }

                        /**
                         * swidプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getSwid() {
                            return swid;
                        }

                        /**
                         * swidプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setSwid(String value) {
                            this.swid = value;
                        }

                        /**
                         * configidプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getConfigid() {
                            return configid;
                        }

                        /**
                         * configidプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setConfigid(String value) {
                            this.configid = value;
                        }

                        /**
                         * vendorプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getVendor() {
                            return vendor;
                        }

                        /**
                         * vendorプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setVendor(String value) {
                            this.vendor = value;
                        }

                        /**
                         * familyプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getFamily() {
                            return family;
                        }

                        /**
                         * familyプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setFamily(String value) {
                            this.family = value;
                        }

                        /**
                         * nameプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getName() {
                            return name;
                        }

                        /**
                         * nameプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setName(String value) {
                            this.name = value;
                        }

                        /**
                         * versionプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getVersion() {
                            return version;
                        }

                        /**
                         * versionプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setVersion(String value) {
                            this.version = value;
                        }

                        /**
                         * patchプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getPatch() {
                            return patch;
                        }

                        /**
                         * patchプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setPatch(String value) {
                            this.patch = value;
                        }

                    }


                    /**
                     * <p>anonymous complex typeのJavaクラス。
                     * 
                     * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                     * 
                     * <pre>
                     * &lt;complexType>
                     *   &lt;complexContent>
                     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                     *       &lt;sequence>
                     *         &lt;element name="Port" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *         &lt;element name="Portlist" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *         &lt;element name="ProtoType" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *         &lt;element name="ProtoCode" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *         &lt;element name="ProtoField" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *         &lt;element name="Application" maxOccurs="unbounded" minOccurs="0">
                     *           &lt;complexType>
                     *             &lt;complexContent>
                     *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                     *                 &lt;sequence>
                     *                   &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                     *                 &lt;/sequence>
                     *                 &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *                 &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *               &lt;/restriction>
                     *             &lt;/complexContent>
                     *           &lt;/complexType>
                     *         &lt;/element>
                     *       &lt;/sequence>
                     *       &lt;attribute name="ip_protocol" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *     &lt;/restriction>
                     *   &lt;/complexContent>
                     * &lt;/complexType>
                     * </pre>
                     * 
                     * 
                     */
                    @XmlAccessorType(XmlAccessType.FIELD)
                    @XmlType(name = "", propOrder = {
                        "port",
                        "portlist",
                        "protoType",
                        "protoCode",
                        "protoField",
                        "application"
                    })
                    public static class Service {

                        @XmlElement(name = "Port")
                        protected String port;
                        @XmlElement(name = "Portlist")
                        protected String portlist;
                        @XmlElement(name = "ProtoType")
                        protected String protoType;
                        @XmlElement(name = "ProtoCode")
                        protected String protoCode;
                        @XmlElement(name = "ProtoField")
                        protected String protoField;
                        @XmlElement(name = "Application")
                        protected List<IODEFDocument.Incident.EventData.Flow.System.Service.Application> application;
                        @XmlAttribute(name = "ip_protocol")
                        protected String ipProtocol;

                        /**
                         * portプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getPort() {
                            return port;
                        }

                        /**
                         * portプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setPort(String value) {
                            this.port = value;
                        }

                        /**
                         * portlistプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getPortlist() {
                            return portlist;
                        }

                        /**
                         * portlistプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setPortlist(String value) {
                            this.portlist = value;
                        }

                        /**
                         * protoTypeプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getProtoType() {
                            return protoType;
                        }

                        /**
                         * protoTypeプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setProtoType(String value) {
                            this.protoType = value;
                        }

                        /**
                         * protoCodeプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getProtoCode() {
                            return protoCode;
                        }

                        /**
                         * protoCodeプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setProtoCode(String value) {
                            this.protoCode = value;
                        }

                        /**
                         * protoFieldプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getProtoField() {
                            return protoField;
                        }

                        /**
                         * protoFieldプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setProtoField(String value) {
                            this.protoField = value;
                        }

                        /**
                         * Gets the value of the application property.
                         * 
                         * <p>
                         * This accessor method returns a reference to the live list,
                         * not a snapshot. Therefore any modification you make to the
                         * returned list will be present inside the JAXB object.
                         * This is why there is not a <CODE>set</CODE> method for the application property.
                         * 
                         * <p>
                         * For example, to add a new item, do as follows:
                         * <pre>
                         *    getApplication().add(newItem);
                         * </pre>
                         * 
                         * 
                         * <p>
                         * Objects of the following type(s) are allowed in the list
                         * {@link IODEFDocument.Incident.EventData.Flow.System.Service.Application }
                         * 
                         * 
                         */
                        public List<IODEFDocument.Incident.EventData.Flow.System.Service.Application> getApplication() {
                            if (application == null) {
                                application = new ArrayList<IODEFDocument.Incident.EventData.Flow.System.Service.Application>();
                            }
                            return this.application;
                        }

                        /**
                         * ipProtocolプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getIpProtocol() {
                            return ipProtocol;
                        }

                        /**
                         * ipProtocolプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setIpProtocol(String value) {
                            this.ipProtocol = value;
                        }


                        /**
                         * <p>anonymous complex typeのJavaクラス。
                         * 
                         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                         * 
                         * <pre>
                         * &lt;complexType>
                         *   &lt;complexContent>
                         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                         *       &lt;sequence>
                         *         &lt;element name="URL" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                         *       &lt;/sequence>
                         *       &lt;attribute name="swid" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="configid" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="vendor" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="family" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="name" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="version" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *       &lt;attribute name="patch" type="{http://www.w3.org/2001/XMLSchema}string" />
                         *     &lt;/restriction>
                         *   &lt;/complexContent>
                         * &lt;/complexType>
                         * </pre>
                         * 
                         * 
                         */
                        @XmlAccessorType(XmlAccessType.FIELD)
                        @XmlType(name = "", propOrder = {
                            "url"
                        })
                        public static class Application {

                            @XmlElement(name = "URL")
                            protected String url;
                            @XmlAttribute(name = "swid")
                            protected String swid;
                            @XmlAttribute(name = "configid")
                            protected String configid;
                            @XmlAttribute(name = "vendor")
                            protected String vendor;
                            @XmlAttribute(name = "family")
                            protected String family;
                            @XmlAttribute(name = "name")
                            protected String name;
                            @XmlAttribute(name = "version")
                            protected String version;
                            @XmlAttribute(name = "patch")
                            protected String patch;

                            /**
                             * urlプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getURL() {
                                return url;
                            }

                            /**
                             * urlプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setURL(String value) {
                                this.url = value;
                            }

                            /**
                             * swidプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getSwid() {
                                return swid;
                            }

                            /**
                             * swidプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setSwid(String value) {
                                this.swid = value;
                            }

                            /**
                             * configidプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getConfigid() {
                                return configid;
                            }

                            /**
                             * configidプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setConfigid(String value) {
                                this.configid = value;
                            }

                            /**
                             * vendorプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getVendor() {
                                return vendor;
                            }

                            /**
                             * vendorプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setVendor(String value) {
                                this.vendor = value;
                            }

                            /**
                             * familyプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getFamily() {
                                return family;
                            }

                            /**
                             * familyプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setFamily(String value) {
                                this.family = value;
                            }

                            /**
                             * nameプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getName() {
                                return name;
                            }

                            /**
                             * nameプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setName(String value) {
                                this.name = value;
                            }

                            /**
                             * versionプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getVersion() {
                                return version;
                            }

                            /**
                             * versionプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setVersion(String value) {
                                this.version = value;
                            }

                            /**
                             * patchプロパティの値を取得します。
                             * 
                             * @return
                             *     possible object is
                             *     {@link String }
                             *     
                             */
                            public String getPatch() {
                                return patch;
                            }

                            /**
                             * patchプロパティの値を設定します。
                             * 
                             * @param value
                             *     allowed object is
                             *     {@link String }
                             *     
                             */
                            public void setPatch(String value) {
                                this.patch = value;
                            }

                        }

                    }

                }

            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;complexContent>
             *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *       &lt;sequence>
             *         &lt;element name="RecordData" maxOccurs="unbounded" minOccurs="0">
             *           &lt;complexType>
             *             &lt;complexContent>
             *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *                 &lt;sequence>
             *                   &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *                   &lt;element name="RecordPattern" maxOccurs="unbounded" minOccurs="0">
             *                     &lt;complexType>
             *                       &lt;simpleContent>
             *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *                           &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="offset" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="ext-offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="instance" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                         &lt;/extension>
             *                       &lt;/simpleContent>
             *                     &lt;/complexType>
             *                   &lt;/element>
             *                   &lt;element name="RecordItem" maxOccurs="unbounded" minOccurs="0">
             *                     &lt;complexType>
             *                       &lt;simpleContent>
             *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *                           &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                           &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
             *                         &lt;/extension>
             *                       &lt;/simpleContent>
             *                     &lt;/complexType>
             *                   &lt;/element>
             *                 &lt;/sequence>
             *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
             *               &lt;/restriction>
             *             &lt;/complexContent>
             *           &lt;/complexType>
             *         &lt;/element>
             *       &lt;/sequence>
             *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/restriction>
             *   &lt;/complexContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "recordData"
            })
            public static class Record {

                @XmlElement(name = "RecordData")
                protected List<IODEFDocument.Incident.EventData.Record.RecordData> recordData;
                @XmlAttribute(name = "restriction")
                protected String restriction;

                /**
                 * Gets the value of the recordData property.
                 * 
                 * <p>
                 * This accessor method returns a reference to the live list,
                 * not a snapshot. Therefore any modification you make to the
                 * returned list will be present inside the JAXB object.
                 * This is why there is not a <CODE>set</CODE> method for the recordData property.
                 * 
                 * <p>
                 * For example, to add a new item, do as follows:
                 * <pre>
                 *    getRecordData().add(newItem);
                 * </pre>
                 * 
                 * 
                 * <p>
                 * Objects of the following type(s) are allowed in the list
                 * {@link IODEFDocument.Incident.EventData.Record.RecordData }
                 * 
                 * 
                 */
                public List<IODEFDocument.Incident.EventData.Record.RecordData> getRecordData() {
                    if (recordData == null) {
                        recordData = new ArrayList<IODEFDocument.Incident.EventData.Record.RecordData>();
                    }
                    return this.recordData;
                }

                /**
                 * restrictionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getRestriction() {
                    return restriction;
                }

                /**
                 * restrictionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setRestriction(String value) {
                    this.restriction = value;
                }


                /**
                 * <p>anonymous complex typeのJavaクラス。
                 * 
                 * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                 * 
                 * <pre>
                 * &lt;complexType>
                 *   &lt;complexContent>
                 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
                 *       &lt;sequence>
                 *         &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
                 *         &lt;element name="RecordPattern" maxOccurs="unbounded" minOccurs="0">
                 *           &lt;complexType>
                 *             &lt;simpleContent>
                 *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *                 &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="offset" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="ext-offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="instance" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *               &lt;/extension>
                 *             &lt;/simpleContent>
                 *           &lt;/complexType>
                 *         &lt;/element>
                 *         &lt;element name="RecordItem" maxOccurs="unbounded" minOccurs="0">
                 *           &lt;complexType>
                 *             &lt;simpleContent>
                 *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *                 &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *               &lt;/extension>
                 *             &lt;/simpleContent>
                 *           &lt;/complexType>
                 *         &lt;/element>
                 *       &lt;/sequence>
                 *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *     &lt;/restriction>
                 *   &lt;/complexContent>
                 * &lt;/complexType>
                 * </pre>
                 * 
                 * 
                 */
                @XmlAccessorType(XmlAccessType.FIELD)
                @XmlType(name = "", propOrder = {
                    "dateTime",
                    "recordPattern",
                    "recordItem"
                })
                public static class RecordData {

                    @XmlElement(name = "DateTime")
                    protected String dateTime;
                    @XmlElement(name = "RecordPattern", nillable = true)
                    protected List<IODEFDocument.Incident.EventData.Record.RecordData.RecordPattern> recordPattern;
                    @XmlElement(name = "RecordItem", nillable = true)
                    protected List<IODEFDocument.Incident.EventData.Record.RecordData.RecordItem> recordItem;
                    @XmlAttribute(name = "restriction")
                    protected String restriction;

                    /**
                     * dateTimeプロパティの値を取得します。
                     * 
                     * @return
                     *     possible object is
                     *     {@link String }
                     *     
                     */
                    public String getDateTime() {
                        return dateTime;
                    }

                    /**
                     * dateTimeプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setDateTime(String value) {
                        this.dateTime = value;
                    }

                    /**
                     * Gets the value of the recordPattern property.
                     * 
                     * <p>
                     * This accessor method returns a reference to the live list,
                     * not a snapshot. Therefore any modification you make to the
                     * returned list will be present inside the JAXB object.
                     * This is why there is not a <CODE>set</CODE> method for the recordPattern property.
                     * 
                     * <p>
                     * For example, to add a new item, do as follows:
                     * <pre>
                     *    getRecordPattern().add(newItem);
                     * </pre>
                     * 
                     * 
                     * <p>
                     * Objects of the following type(s) are allowed in the list
                     * {@link IODEFDocument.Incident.EventData.Record.RecordData.RecordPattern }
                     * 
                     * 
                     */
                    public List<IODEFDocument.Incident.EventData.Record.RecordData.RecordPattern> getRecordPattern() {
                        if (recordPattern == null) {
                            recordPattern = new ArrayList<IODEFDocument.Incident.EventData.Record.RecordData.RecordPattern>();
                        }
                        return this.recordPattern;
                    }

                    /**
                     * Gets the value of the recordItem property.
                     * 
                     * <p>
                     * This accessor method returns a reference to the live list,
                     * not a snapshot. Therefore any modification you make to the
                     * returned list will be present inside the JAXB object.
                     * This is why there is not a <CODE>set</CODE> method for the recordItem property.
                     * 
                     * <p>
                     * For example, to add a new item, do as follows:
                     * <pre>
                     *    getRecordItem().add(newItem);
                     * </pre>
                     * 
                     * 
                     * <p>
                     * Objects of the following type(s) are allowed in the list
                     * {@link IODEFDocument.Incident.EventData.Record.RecordData.RecordItem }
                     * 
                     * 
                     */
                    public List<IODEFDocument.Incident.EventData.Record.RecordData.RecordItem> getRecordItem() {
                        if (recordItem == null) {
                            recordItem = new ArrayList<IODEFDocument.Incident.EventData.Record.RecordData.RecordItem>();
                        }
                        return this.recordItem;
                    }

                    /**
                     * restrictionプロパティの値を取得します。
                     * 
                     * @return
                     *     possible object is
                     *     {@link String }
                     *     
                     */
                    public String getRestriction() {
                        return restriction;
                    }

                    /**
                     * restrictionプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setRestriction(String value) {
                        this.restriction = value;
                    }


                    /**
                     * <p>anonymous complex typeのJavaクラス。
                     * 
                     * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                     * 
                     * <pre>
                     * &lt;complexType>
                     *   &lt;simpleContent>
                     *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                     *       &lt;attribute name="dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="ext-dtype" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="meaning" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="formatid" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *     &lt;/extension>
                     *   &lt;/simpleContent>
                     * &lt;/complexType>
                     * </pre>
                     * 
                     * 
                     */
                    @XmlAccessorType(XmlAccessType.FIELD)
                    @XmlType(name = "", propOrder = {
                        "value"
                    })
                    public static class RecordItem {

                        @XmlValue
                        protected String value;
                        @XmlAttribute(name = "dtype")
                        protected String dtype;
                        @XmlAttribute(name = "ext-dtype")
                        protected String extDtype;
                        @XmlAttribute(name = "meaning")
                        protected String meaning;
                        @XmlAttribute(name = "formatid")
                        protected String formatid;
                        @XmlAttribute(name = "restriction")
                        protected String restriction;

                        /**
                         * valueプロパティの値を取得します。
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
                         * valueプロパティの値を設定します。
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
                         * dtypeプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getDtype() {
                            return dtype;
                        }

                        /**
                         * dtypeプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setDtype(String value) {
                            this.dtype = value;
                        }

                        /**
                         * extDtypeプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getExtDtype() {
                            return extDtype;
                        }

                        /**
                         * extDtypeプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setExtDtype(String value) {
                            this.extDtype = value;
                        }

                        /**
                         * meaningプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getMeaning() {
                            return meaning;
                        }

                        /**
                         * meaningプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setMeaning(String value) {
                            this.meaning = value;
                        }

                        /**
                         * formatidプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getFormatid() {
                            return formatid;
                        }

                        /**
                         * formatidプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setFormatid(String value) {
                            this.formatid = value;
                        }

                        /**
                         * restrictionプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getRestriction() {
                            return restriction;
                        }

                        /**
                         * restrictionプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setRestriction(String value) {
                            this.restriction = value;
                        }

                    }


                    /**
                     * <p>anonymous complex typeのJavaクラス。
                     * 
                     * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                     * 
                     * <pre>
                     * &lt;complexType>
                     *   &lt;simpleContent>
                     *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                     *       &lt;attribute name="type" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="ext-type" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="offset" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="ext-offsetunit" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *       &lt;attribute name="instance" type="{http://www.w3.org/2001/XMLSchema}string" />
                     *     &lt;/extension>
                     *   &lt;/simpleContent>
                     * &lt;/complexType>
                     * </pre>
                     * 
                     * 
                     */
                    @XmlAccessorType(XmlAccessType.FIELD)
                    @XmlType(name = "", propOrder = {
                        "value"
                    })
                    public static class RecordPattern {

                        @XmlValue
                        protected String value;
                        @XmlAttribute(name = "type")
                        protected String type;
                        @XmlAttribute(name = "ext-type")
                        protected String extType;
                        @XmlAttribute(name = "offset")
                        protected String offset;
                        @XmlAttribute(name = "offsetunit")
                        protected String offsetunit;
                        @XmlAttribute(name = "ext-offsetunit")
                        protected String extOffsetunit;
                        @XmlAttribute(name = "instance")
                        protected String instance;

                        /**
                         * valueプロパティの値を取得します。
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
                         * valueプロパティの値を設定します。
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
                         * typeプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getType() {
                            return type;
                        }

                        /**
                         * typeプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setType(String value) {
                            this.type = value;
                        }

                        /**
                         * extTypeプロパティの値を取得します。
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
                         * extTypeプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setExtType(String value) {
                            this.extType = value;
                        }

                        /**
                         * offsetプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getOffset() {
                            return offset;
                        }

                        /**
                         * offsetプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setOffset(String value) {
                            this.offset = value;
                        }

                        /**
                         * offsetunitプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getOffsetunit() {
                            return offsetunit;
                        }

                        /**
                         * offsetunitプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setOffsetunit(String value) {
                            this.offsetunit = value;
                        }

                        /**
                         * extOffsetunitプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getExtOffsetunit() {
                            return extOffsetunit;
                        }

                        /**
                         * extOffsetunitプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setExtOffsetunit(String value) {
                            this.extOffsetunit = value;
                        }

                        /**
                         * instanceプロパティの値を取得します。
                         * 
                         * @return
                         *     possible object is
                         *     {@link String }
                         *     
                         */
                        public String getInstance() {
                            return instance;
                        }

                        /**
                         * instanceプロパティの値を設定します。
                         * 
                         * @param value
                         *     allowed object is
                         *     {@link String }
                         *     
                         */
                        public void setInstance(String value) {
                            this.instance = value;
                        }

                    }

                }

            }

        }


        /**
         * <p>anonymous complex typeのJavaクラス。
         * 
         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;complexContent>
         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *       &lt;sequence>
         *         &lt;element name="HistoryItem" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;complexContent>
         *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                 &lt;sequence>
         *                   &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
         *                 &lt;/sequence>
         *                 &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                 &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
         *               &lt;/restriction>
         *             &lt;/complexContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *       &lt;/sequence>
         *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/restriction>
         *   &lt;/complexContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "", propOrder = {
            "historyItem"
        })
        public static class History {

            @XmlElement(name = "HistoryItem")
            protected List<IODEFDocument.Incident.History.HistoryItem> historyItem;
            @XmlAttribute(name = "restriction")
            protected String restriction;

            /**
             * Gets the value of the historyItem property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the historyItem property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getHistoryItem().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.History.HistoryItem }
             * 
             * 
             */
            public List<IODEFDocument.Incident.History.HistoryItem> getHistoryItem() {
                if (historyItem == null) {
                    historyItem = new ArrayList<IODEFDocument.Incident.History.HistoryItem>();
                }
                return this.historyItem;
            }

            /**
             * restrictionプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRestriction() {
                return restriction;
            }

            /**
             * restrictionプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRestriction(String value) {
                this.restriction = value;
            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;complexContent>
             *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *       &lt;sequence>
             *         &lt;element name="DateTime" type="{http://www.w3.org/2001/XMLSchema}string" minOccurs="0"/>
             *       &lt;/sequence>
             *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="action" type="{http://www.w3.org/2001/XMLSchema}string" />
             *       &lt;attribute name="ext-action" type="{http://www.w3.org/2001/XMLSchema}string" />
             *     &lt;/restriction>
             *   &lt;/complexContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "dateTime"
            })
            public static class HistoryItem {

                @XmlElement(name = "DateTime")
                protected String dateTime;
                @XmlAttribute(name = "restriction")
                protected String restriction;
                @XmlAttribute(name = "action")
                protected String action;
                @XmlAttribute(name = "ext-action")
                protected String extAction;

                /**
                 * dateTimeプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getDateTime() {
                    return dateTime;
                }

                /**
                 * dateTimeプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setDateTime(String value) {
                    this.dateTime = value;
                }

                /**
                 * restrictionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getRestriction() {
                    return restriction;
                }

                /**
                 * restrictionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setRestriction(String value) {
                    this.restriction = value;
                }

                /**
                 * actionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getAction() {
                    return action;
                }

                /**
                 * actionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setAction(String value) {
                    this.action = value;
                }

                /**
                 * extActionプロパティの値を取得します。
                 * 
                 * @return
                 *     possible object is
                 *     {@link String }
                 *     
                 */
                public String getExtAction() {
                    return extAction;
                }

                /**
                 * extActionプロパティの値を設定します。
                 * 
                 * @param value
                 *     allowed object is
                 *     {@link String }
                 *     
                 */
                public void setExtAction(String value) {
                    this.extAction = value;
                }

            }

        }


        /**
         * <p>anonymous complex typeのJavaクラス。
         * 
         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;complexContent>
         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *       &lt;sequence>
         *         &lt;element name="Reference" maxOccurs="unbounded" minOccurs="0">
         *           &lt;complexType>
         *             &lt;complexContent>
         *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *                 &lt;sequence>
         *                   &lt;element name="ReferenceName" maxOccurs="unbounded" minOccurs="0">
         *                     &lt;complexType>
         *                       &lt;simpleContent>
         *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                           &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
         *                         &lt;/extension>
         *                       &lt;/simpleContent>
         *                     &lt;/complexType>
         *                   &lt;/element>
         *                   &lt;element name="URL" maxOccurs="unbounded" minOccurs="0">
         *                     &lt;complexType>
         *                       &lt;simpleContent>
         *                         &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
         *                         &lt;/extension>
         *                       &lt;/simpleContent>
         *                     &lt;/complexType>
         *                   &lt;/element>
         *                 &lt;/sequence>
         *               &lt;/restriction>
         *             &lt;/complexContent>
         *           &lt;/complexType>
         *         &lt;/element>
         *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}Description" maxOccurs="unbounded" minOccurs="0"/>
         *       &lt;/sequence>
         *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/restriction>
         *   &lt;/complexContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "", propOrder = {
            "reference",
            "description"
        })
        public static class Method {

            @XmlElement(name = "Reference")
            protected List<IODEFDocument.Incident.Method.Reference> reference;
            @XmlElement(name = "Description", nillable = true)
            protected List<Description> description;
            @XmlAttribute(name = "restriction")
            protected String restriction;

            /**
             * Gets the value of the reference property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the reference property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getReference().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IODEFDocument.Incident.Method.Reference }
             * 
             * 
             */
            public List<IODEFDocument.Incident.Method.Reference> getReference() {
                if (reference == null) {
                    reference = new ArrayList<IODEFDocument.Incident.Method.Reference>();
                }
                return this.reference;
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
             * {@link Description }
             * 
             * 
             */
            public List<Description> getDescription() {
                if (description == null) {
                    description = new ArrayList<Description>();
                }
                return this.description;
            }

            /**
             * restrictionプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRestriction() {
                return restriction;
            }

            /**
             * restrictionプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRestriction(String value) {
                this.restriction = value;
            }


            /**
             * <p>anonymous complex typeのJavaクラス。
             * 
             * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
             * 
             * <pre>
             * &lt;complexType>
             *   &lt;complexContent>
             *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
             *       &lt;sequence>
             *         &lt;element name="ReferenceName" maxOccurs="unbounded" minOccurs="0">
             *           &lt;complexType>
             *             &lt;simpleContent>
             *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *                 &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
             *               &lt;/extension>
             *             &lt;/simpleContent>
             *           &lt;/complexType>
             *         &lt;/element>
             *         &lt;element name="URL" maxOccurs="unbounded" minOccurs="0">
             *           &lt;complexType>
             *             &lt;simpleContent>
             *               &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
             *               &lt;/extension>
             *             &lt;/simpleContent>
             *           &lt;/complexType>
             *         &lt;/element>
             *       &lt;/sequence>
             *     &lt;/restriction>
             *   &lt;/complexContent>
             * &lt;/complexType>
             * </pre>
             * 
             * 
             */
            @XmlAccessorType(XmlAccessType.FIELD)
            @XmlType(name = "", propOrder = {
                "referenceName",
                "url"
            })
            public static class Reference {

                @XmlElement(name = "ReferenceName", nillable = true)
                protected List<IODEFDocument.Incident.Method.Reference.ReferenceName> referenceName;
                @XmlElement(name = "URL", nillable = true)
                protected List<IODEFDocument.Incident.Method.Reference.URL> url;

                /**
                 * Gets the value of the referenceName property.
                 * 
                 * <p>
                 * This accessor method returns a reference to the live list,
                 * not a snapshot. Therefore any modification you make to the
                 * returned list will be present inside the JAXB object.
                 * This is why there is not a <CODE>set</CODE> method for the referenceName property.
                 * 
                 * <p>
                 * For example, to add a new item, do as follows:
                 * <pre>
                 *    getReferenceName().add(newItem);
                 * </pre>
                 * 
                 * 
                 * <p>
                 * Objects of the following type(s) are allowed in the list
                 * {@link IODEFDocument.Incident.Method.Reference.ReferenceName }
                 * 
                 * 
                 */
                public List<IODEFDocument.Incident.Method.Reference.ReferenceName> getReferenceName() {
                    if (referenceName == null) {
                        referenceName = new ArrayList<IODEFDocument.Incident.Method.Reference.ReferenceName>();
                    }
                    return this.referenceName;
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
                 * {@link IODEFDocument.Incident.Method.Reference.URL }
                 * 
                 * 
                 */
                public List<IODEFDocument.Incident.Method.Reference.URL> getURL() {
                    if (url == null) {
                        url = new ArrayList<IODEFDocument.Incident.Method.Reference.URL>();
                    }
                    return this.url;
                }


                /**
                 * <p>anonymous complex typeのJavaクラス。
                 * 
                 * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                 * 
                 * <pre>
                 * &lt;complexType>
                 *   &lt;simpleContent>
                 *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *       &lt;attribute name="lang" type="{http://www.w3.org/2001/XMLSchema}string" />
                 *     &lt;/extension>
                 *   &lt;/simpleContent>
                 * &lt;/complexType>
                 * </pre>
                 * 
                 * 
                 */
                @XmlAccessorType(XmlAccessType.FIELD)
                @XmlType(name = "", propOrder = {
                    "value"
                })
                public static class ReferenceName {

                    @XmlValue
                    protected String value;
                    @XmlAttribute(name = "lang")
                    protected String lang;

                    /**
                     * valueプロパティの値を取得します。
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
                     * valueプロパティの値を設定します。
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
                     * langプロパティの値を取得します。
                     * 
                     * @return
                     *     possible object is
                     *     {@link String }
                     *     
                     */
                    public String getLang() {
                        return lang;
                    }

                    /**
                     * langプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setLang(String value) {
                        this.lang = value;
                    }

                }


                /**
                 * <p>anonymous complex typeのJavaクラス。
                 * 
                 * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
                 * 
                 * <pre>
                 * &lt;complexType>
                 *   &lt;simpleContent>
                 *     &lt;extension base="&lt;http://www.w3.org/2001/XMLSchema>string">
                 *     &lt;/extension>
                 *   &lt;/simpleContent>
                 * &lt;/complexType>
                 * </pre>
                 * 
                 * 
                 */
                @XmlAccessorType(XmlAccessType.FIELD)
                @XmlType(name = "", propOrder = {
                    "value"
                })
                public static class URL {

                    @XmlValue
                    protected String value;

                    /**
                     * valueプロパティの値を取得します。
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
                     * valueプロパティの値を設定します。
                     * 
                     * @param value
                     *     allowed object is
                     *     {@link String }
                     *     
                     */
                    public void setValue(String value) {
                        this.value = value;
                    }

                }

            }

        }


        /**
         * <p>anonymous complex typeのJavaクラス。
         * 
         * <p>次のスキーマ・フラグメントは、このクラス内に含まれる予期されるコンテンツを指定します。
         * 
         * <pre>
         * &lt;complexType>
         *   &lt;complexContent>
         *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
         *       &lt;sequence>
         *         &lt;element ref="{urn:ietf:params:xml:ns:iodef-1.0}IncidentID" maxOccurs="unbounded" minOccurs="0"/>
         *       &lt;/sequence>
         *       &lt;attribute name="restriction" type="{http://www.w3.org/2001/XMLSchema}string" />
         *     &lt;/restriction>
         *   &lt;/complexContent>
         * &lt;/complexType>
         * </pre>
         * 
         * 
         */
        @XmlAccessorType(XmlAccessType.FIELD)
        @XmlType(name = "", propOrder = {
            "incidentID"
        })
        public static class RelatedActivity {

            @XmlElement(name = "IncidentID", nillable = true)
            protected List<IncidentID> incidentID;
            @XmlAttribute(name = "restriction")
            protected String restriction;

            /**
             * Gets the value of the incidentID property.
             * 
             * <p>
             * This accessor method returns a reference to the live list,
             * not a snapshot. Therefore any modification you make to the
             * returned list will be present inside the JAXB object.
             * This is why there is not a <CODE>set</CODE> method for the incidentID property.
             * 
             * <p>
             * For example, to add a new item, do as follows:
             * <pre>
             *    getIncidentID().add(newItem);
             * </pre>
             * 
             * 
             * <p>
             * Objects of the following type(s) are allowed in the list
             * {@link IncidentID }
             * 
             * 
             */
            public List<IncidentID> getIncidentID() {
                if (incidentID == null) {
                    incidentID = new ArrayList<IncidentID>();
                }
                return this.incidentID;
            }

            /**
             * restrictionプロパティの値を取得します。
             * 
             * @return
             *     possible object is
             *     {@link String }
             *     
             */
            public String getRestriction() {
                return restriction;
            }

            /**
             * restrictionプロパティの値を設定します。
             * 
             * @param value
             *     allowed object is
             *     {@link String }
             *     
             */
            public void setRestriction(String value) {
                this.restriction = value;
            }

        }

    }

}
