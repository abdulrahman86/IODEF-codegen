# ./iodef-03.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:53f1f331c5e33f9a04da8bb294eb2d0780d80992
# Generated 2014-02-11 12:53:43.305174 by PyXB version 1.2.3
# Namespace urn:ietf:params:xml:ns:iodef-1.0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:199e7904-92d0-11e3-b911-001517d2ceb0')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'urn:ietf:params:xml:ns:iodef-1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 4, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 7, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 7, 10)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute instance uses Python identifier instance
    __instance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instance'), 'instance', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_instance', pyxb.binding.datatypes.string)
    __instance._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 8, 10)
    __instance._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 8, 10)
    
    instance = property(__instance.value, __instance.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 9, 10)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 9, 10)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __instance.name() : __instance,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 15, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON__lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 18, 10)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 18, 10)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_2_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 27, 10)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 27, 10)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 33, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Incident uses Python identifier Incident
    __Incident = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Incident'), 'Incident', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_urnietfparamsxmlnsiodef_1_0Incident', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 35, 8), )

    
    Incident = property(__Incident.value, __Incident.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 433, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 433, 6)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 434, 6)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 434, 6)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute formatid uses Python identifier formatid
    __formatid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatid'), 'formatid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_formatid', pyxb.binding.datatypes.string)
    __formatid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 435, 6)
    __formatid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 435, 6)
    
    formatid = property(__formatid.value, __formatid.set, None, None)

    _ElementMap.update({
        __Incident.name() : __Incident
    })
    _AttributeMap.update({
        __version.name() : __version,
        __lang.name() : __lang,
        __formatid.name() : __formatid
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 36, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 14, 2), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DetectTime uses Python identifier DetectTime
    __DetectTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), 'DetectTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0DetectTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 38, 14), )

    
    DetectTime = property(__DetectTime.value, __DetectTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 39, 14), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 40, 14), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ReportTime uses Python identifier ReportTime
    __ReportTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), 'ReportTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0ReportTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 41, 14), )

    
    ReportTime = property(__ReportTime.value, __ReportTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AlternativeID uses Python identifier AlternativeID
    __AlternativeID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), 'AlternativeID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0AlternativeID', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 43, 14), )

    
    AlternativeID = property(__AlternativeID.value, __AlternativeID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RelatedActivity uses Python identifier RelatedActivity
    __RelatedActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), 'RelatedActivity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0RelatedActivity', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 51, 14), )

    
    RelatedActivity = property(__RelatedActivity.value, __RelatedActivity.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Assessment uses Python identifier Assessment
    __Assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), 'Assessment', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0Assessment', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 60, 14), )

    
    Assessment = property(__Assessment.value, __Assessment.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Method uses Python identifier Method
    __Method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Method'), 'Method', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0Method', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 139, 14), )

    
    Method = property(__Method.value, __Method.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 170, 14), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EventData uses Python identifier EventData
    __EventData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventData'), 'EventData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0EventData', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 238, 14), )

    
    EventData = property(__EventData.value, __EventData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}History uses Python identifier History
    __History = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'History'), 'History', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0History', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 408, 14), )

    
    History = property(__History.value, __History.set, None, None)

    
    # Attribute purpose uses Python identifier purpose
    __purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'purpose'), 'purpose', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_purpose', pyxb.binding.datatypes.string)
    __purpose._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 426, 12)
    __purpose._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 426, 12)
    
    purpose = property(__purpose.value, __purpose.set, None, None)

    
    # Attribute ext_purpose uses Python identifier ext_purpose
    __ext_purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_purpose'), 'ext_purpose', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_ext_purpose', pyxb.binding.datatypes.string)
    __ext_purpose._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 427, 12)
    __ext_purpose._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 427, 12)
    
    ext_purpose = property(__ext_purpose.value, __ext_purpose.set, None, None)

    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 428, 12)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 428, 12)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 429, 12)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 429, 12)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID,
        __Description.name() : __Description,
        __DetectTime.name() : __DetectTime,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __ReportTime.name() : __ReportTime,
        __AlternativeID.name() : __AlternativeID,
        __RelatedActivity.name() : __RelatedActivity,
        __Assessment.name() : __Assessment,
        __Method.name() : __Method,
        __Contact.name() : __Contact,
        __EventData.name() : __EventData,
        __History.name() : __History
    })
    _AttributeMap.update({
        __purpose.name() : __purpose,
        __ext_purpose.name() : __ext_purpose,
        __lang.name() : __lang,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 44, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 48, 18)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 48, 18)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 52, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_6_urnietfparamsxmlnsiodef_1_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_6_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 56, 18)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 56, 18)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 61, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Impact uses Python identifier Impact
    __Impact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Impact'), 'Impact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0Impact', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 63, 20), )

    
    Impact = property(__Impact.value, __Impact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}TimeImpact uses Python identifier TimeImpact
    __TimeImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), 'TimeImpact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0TimeImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 76, 20), )

    
    TimeImpact = property(__TimeImpact.value, __TimeImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}MonetaryImpact uses Python identifier MonetaryImpact
    __MonetaryImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), 'MonetaryImpact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0MonetaryImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 89, 20), )

    
    MonetaryImpact = property(__MonetaryImpact.value, __MonetaryImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0Counter', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 99, 20), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Confidence uses Python identifier Confidence
    __Confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), 'Confidence', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0Confidence', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 112, 20), )

    
    Confidence = property(__Confidence.value, __Confidence.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 121, 20), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Attribute occurrence uses Python identifier occurrence
    __occurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'occurrence'), 'occurrence', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_occurrence', pyxb.binding.datatypes.string)
    __occurrence._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 135, 18)
    __occurrence._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 135, 18)
    
    occurrence = property(__occurrence.value, __occurrence.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 136, 18)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 136, 18)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __Impact.name() : __Impact,
        __TimeImpact.name() : __TimeImpact,
        __MonetaryImpact.name() : __MonetaryImpact,
        __Counter.name() : __Counter,
        __Confidence.name() : __Confidence,
        __AdditionalData.name() : __AdditionalData
    })
    _AttributeMap.update({
        __occurrence.name() : __occurrence,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 64, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_severity', pyxb.binding.datatypes.string)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 67, 28)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 67, 28)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute completion uses Python identifier completion
    __completion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'completion'), 'completion', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_completion', pyxb.binding.datatypes.string)
    __completion._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 68, 28)
    __completion._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 68, 28)
    
    completion = property(__completion.value, __completion.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 69, 28)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 69, 28)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext_type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 70, 28)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 70, 28)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 71, 28)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 71, 28)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __completion.name() : __completion,
        __type.name() : __type,
        __ext_type.name() : __ext_type,
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 77, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_9_severity', pyxb.binding.datatypes.string)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 80, 28)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 80, 28)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute metric uses Python identifier metric
    __metric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'metric'), 'metric', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_9_metric', pyxb.binding.datatypes.string)
    __metric._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 81, 28)
    __metric._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 81, 28)
    
    metric = property(__metric.value, __metric.set, None, None)

    
    # Attribute ext_metric uses Python identifier ext_metric
    __ext_metric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_metric'), 'ext_metric', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_9_ext_metric', pyxb.binding.datatypes.string)
    __ext_metric._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 82, 28)
    __ext_metric._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 82, 28)
    
    ext_metric = property(__ext_metric.value, __ext_metric.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_9_duration', pyxb.binding.datatypes.string)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 83, 28)
    __duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 83, 28)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute ext_duration uses Python identifier ext_duration
    __ext_duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_duration'), 'ext_duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_9_ext_duration', pyxb.binding.datatypes.string)
    __ext_duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 84, 28)
    __ext_duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 84, 28)
    
    ext_duration = property(__ext_duration.value, __ext_duration.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __metric.name() : __metric,
        __ext_metric.name() : __ext_metric,
        __duration.name() : __duration,
        __ext_duration.name() : __ext_duration
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 90, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_10_severity', pyxb.binding.datatypes.string)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 93, 28)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 93, 28)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'currency'), 'currency', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_10_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 94, 28)
    __currency._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 94, 28)
    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __currency.name() : __currency
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 100, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_11_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 103, 28)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 103, 28)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext_type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_11_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 104, 28)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 104, 28)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_11_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 105, 28)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 105, 28)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_11_duration', pyxb.binding.datatypes.string)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 106, 28)
    __duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 106, 28)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute ext_duration uses Python identifier ext_duration
    __ext_duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_duration'), 'ext_duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_11_ext_duration', pyxb.binding.datatypes.string)
    __ext_duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 107, 28)
    __ext_duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 107, 28)
    
    ext_duration = property(__ext_duration.value, __ext_duration.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __ext_type.name() : __ext_type,
        __meaning.name() : __meaning,
        __duration.name() : __duration,
        __ext_duration.name() : __ext_duration
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 113, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute rating uses Python identifier rating
    __rating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rating'), 'rating', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_rating', pyxb.binding.datatypes.string)
    __rating._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 116, 28)
    __rating._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 116, 28)
    
    rating = property(__rating.value, __rating.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rating.name() : __rating
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 122, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute dtype uses Python identifier dtype
    __dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dtype'), 'dtype', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_dtype', pyxb.binding.datatypes.string)
    __dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 125, 28)
    __dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 125, 28)
    
    dtype = property(__dtype.value, __dtype.set, None, None)

    
    # Attribute ext_dtype uses Python identifier ext_dtype
    __ext_dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_dtype'), 'ext_dtype', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_ext_dtype', pyxb.binding.datatypes.string)
    __ext_dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 126, 28)
    __ext_dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 126, 28)
    
    ext_dtype = property(__ext_dtype.value, __ext_dtype.set, None, None)

    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 127, 28)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 127, 28)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute formatid uses Python identifier formatid
    __formatid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatid'), 'formatid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_formatid', pyxb.binding.datatypes.string)
    __formatid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 128, 28)
    __formatid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 128, 28)
    
    formatid = property(__formatid.value, __formatid.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 129, 28)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 129, 28)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __dtype.name() : __dtype,
        __ext_dtype.name() : __ext_dtype,
        __meaning.name() : __meaning,
        __formatid.name() : __formatid,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 140, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_14_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 14, 2), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_14_urnietfparamsxmlnsiodef_1_0Reference', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 142, 20), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_14_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 167, 18)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 167, 18)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __Reference.name() : __Reference
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 143, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ReferenceName uses Python identifier ReferenceName
    __ReferenceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReferenceName'), 'ReferenceName', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0ReferenceName', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 145, 26), )

    
    ReferenceName = property(__ReferenceName.value, __ReferenceName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 154, 26), )

    
    URL = property(__URL.value, __URL.set, None, None)

    _ElementMap.update({
        __ReferenceName.name() : __ReferenceName,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 146, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_16_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 149, 34)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 149, 34)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 155, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 171, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Timezone uses Python identifier Timezone
    __Timezone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), 'Timezone', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_urnietfparamsxmlnsiodef_1_0Timezone', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 173, 20), )

    
    Timezone = property(__Timezone.value, __Timezone.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ContactName uses Python identifier ContactName
    __ContactName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), 'ContactName', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_urnietfparamsxmlnsiodef_1_0ContactName', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 174, 20), )

    
    ContactName = property(__ContactName.value, __ContactName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RegistryHandle uses Python identifier RegistryHandle
    __RegistryHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), 'RegistryHandle', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_urnietfparamsxmlnsiodef_1_0RegistryHandle', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 183, 20), )

    
    RegistryHandle = property(__RegistryHandle.value, __RegistryHandle.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}PostalAddress uses Python identifier PostalAddress
    __PostalAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), 'PostalAddress', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_urnietfparamsxmlnsiodef_1_0PostalAddress', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 193, 20), )

    
    PostalAddress = property(__PostalAddress.value, __PostalAddress.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Email'), 'Email', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_urnietfparamsxmlnsiodef_1_0Email', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 203, 20), )

    
    Email = property(__Email.value, __Email.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Telephone uses Python identifier Telephone
    __Telephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), 'Telephone', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_urnietfparamsxmlnsiodef_1_0Telephone', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 212, 20), )

    
    Telephone = property(__Telephone.value, __Telephone.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Fax uses Python identifier Fax
    __Fax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Fax'), 'Fax', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_urnietfparamsxmlnsiodef_1_0Fax', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 221, 20), )

    
    Fax = property(__Fax.value, __Fax.set, None, None)

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_role', pyxb.binding.datatypes.string)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 231, 18)
    __role._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 231, 18)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute ext_role uses Python identifier ext_role
    __ext_role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_role'), 'ext_role', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_ext_role', pyxb.binding.datatypes.string)
    __ext_role._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 232, 18)
    __ext_role._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 232, 18)
    
    ext_role = property(__ext_role.value, __ext_role.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 233, 18)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 233, 18)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext_type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 234, 18)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 234, 18)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 235, 18)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 235, 18)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __Timezone.name() : __Timezone,
        __ContactName.name() : __ContactName,
        __RegistryHandle.name() : __RegistryHandle,
        __PostalAddress.name() : __PostalAddress,
        __Email.name() : __Email,
        __Telephone.name() : __Telephone,
        __Fax.name() : __Fax
    })
    _AttributeMap.update({
        __role.name() : __role,
        __ext_role.name() : __ext_role,
        __type.name() : __type,
        __ext_type.name() : __ext_type,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 175, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_19_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 178, 28)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 178, 28)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 184, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute registry uses Python identifier registry
    __registry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'registry'), 'registry', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_registry', pyxb.binding.datatypes.string)
    __registry._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 187, 28)
    __registry._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 187, 28)
    
    registry = property(__registry.value, __registry.set, None, None)

    
    # Attribute ext_registry uses Python identifier ext_registry
    __ext_registry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_registry'), 'ext_registry', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_ext_registry', pyxb.binding.datatypes.string)
    __ext_registry._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 188, 28)
    __ext_registry._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 188, 28)
    
    ext_registry = property(__ext_registry.value, __ext_registry.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __registry.name() : __registry,
        __ext_registry.name() : __ext_registry
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 194, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 197, 28)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 197, 28)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 198, 28)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 198, 28)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meaning.name() : __meaning,
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 204, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_22_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 207, 28)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 207, 28)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meaning.name() : __meaning
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 213, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_23_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 216, 28)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 216, 28)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meaning.name() : __meaning
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 222, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_24_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 225, 28)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 225, 28)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meaning.name() : __meaning
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 239, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DetectTime uses Python identifier DetectTime
    __DetectTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), 'DetectTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_urnietfparamsxmlnsiodef_1_0DetectTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 241, 20), )

    
    DetectTime = property(__DetectTime.value, __DetectTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_urnietfparamsxmlnsiodef_1_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 242, 20), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_urnietfparamsxmlnsiodef_1_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 243, 20), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Flow uses Python identifier Flow
    __Flow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Flow'), 'Flow', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_urnietfparamsxmlnsiodef_1_0Flow', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 244, 20), )

    
    Flow = property(__Flow.value, __Flow.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Expectation uses Python identifier Expectation
    __Expectation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), 'Expectation', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_urnietfparamsxmlnsiodef_1_0Expectation', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 350, 20), )

    
    Expectation = property(__Expectation.value, __Expectation.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Record uses Python identifier Record
    __Record = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Record'), 'Record', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_urnietfparamsxmlnsiodef_1_0Record', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 362, 20), )

    
    Record = property(__Record.value, __Record.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 405, 18)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 405, 18)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __DetectTime.name() : __DetectTime,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __Flow.name() : __Flow,
        __Expectation.name() : __Expectation,
        __Record.name() : __Record
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 245, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}System uses Python identifier System
    __System = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'System'), 'System', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_urnietfparamsxmlnsiodef_1_0System', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 247, 26), )

    
    System = property(__System.value, __System.set, None, None)

    _ElementMap.update({
        __System.name() : __System
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 248, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Node'), 'Node', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_urnietfparamsxmlnsiodef_1_0Node', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 250, 32), )

    
    Node = property(__Node.value, __Node.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Service'), 'Service', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_urnietfparamsxmlnsiodef_1_0Service', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 299, 32), )

    
    Service = property(__Service.value, __Service.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}OperatingSystem uses Python identifier OperatingSystem
    __OperatingSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), 'OperatingSystem', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_urnietfparamsxmlnsiodef_1_0OperatingSystem', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 325, 32), )

    
    OperatingSystem = property(__OperatingSystem.value, __OperatingSystem.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 340, 30)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 340, 30)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute interface uses Python identifier interface
    __interface = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'interface'), 'interface', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_interface', pyxb.binding.datatypes.string)
    __interface._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 341, 30)
    __interface._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 341, 30)
    
    interface = property(__interface.value, __interface.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_category', pyxb.binding.datatypes.string)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 342, 30)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 342, 30)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext_category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_category'), 'ext_category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 343, 30)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 343, 30)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute spoofed uses Python identifier spoofed
    __spoofed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'spoofed'), 'spoofed', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_spoofed', pyxb.binding.datatypes.string)
    __spoofed._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 344, 30)
    __spoofed._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 344, 30)
    
    spoofed = property(__spoofed.value, __spoofed.set, None, None)

    _ElementMap.update({
        __Node.name() : __Node,
        __Service.name() : __Service,
        __OperatingSystem.name() : __OperatingSystem
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __interface.name() : __interface,
        __category.name() : __category,
        __ext_category.name() : __ext_category,
        __spoofed.name() : __spoofed
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 251, 34)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_28_urnietfparamsxmlnsiodef_1_0Counter', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 253, 38), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_28_urnietfparamsxmlnsiodef_1_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 254, 38), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}NodeName uses Python identifier NodeName
    __NodeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'NodeName'), 'NodeName', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_28_urnietfparamsxmlnsiodef_1_0NodeName', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 255, 38), )

    
    NodeName = property(__NodeName.value, __NodeName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_28_urnietfparamsxmlnsiodef_1_0Address', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 264, 38), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Location'), 'Location', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_28_urnietfparamsxmlnsiodef_1_0Location', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 276, 38), )

    
    Location = property(__Location.value, __Location.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}NodeRole uses Python identifier NodeRole
    __NodeRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), 'NodeRole', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_28_urnietfparamsxmlnsiodef_1_0NodeRole', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 285, 38), )

    
    NodeRole = property(__NodeRole.value, __NodeRole.set, None, None)

    _ElementMap.update({
        __Counter.name() : __Counter,
        __DateTime.name() : __DateTime,
        __NodeName.name() : __NodeName,
        __Address.name() : __Address,
        __Location.name() : __Location,
        __NodeRole.name() : __NodeRole
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 256, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_29_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 259, 46)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 259, 46)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 265, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_30_category', pyxb.binding.datatypes.string)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 268, 46)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 268, 46)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext_category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_category'), 'ext_category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_30_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 269, 46)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 269, 46)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute vlan_name uses Python identifier vlan_name
    __vlan_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vlan_name'), 'vlan_name', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_30_vlan_name', pyxb.binding.datatypes.string)
    __vlan_name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 270, 46)
    __vlan_name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 270, 46)
    
    vlan_name = property(__vlan_name.value, __vlan_name.set, None, None)

    
    # Attribute vlan_num uses Python identifier vlan_num
    __vlan_num = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vlan_num'), 'vlan_num', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_30_vlan_num', pyxb.binding.datatypes.string)
    __vlan_num._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 271, 46)
    __vlan_num._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 271, 46)
    
    vlan_num = property(__vlan_num.value, __vlan_num.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __category.name() : __category,
        __ext_category.name() : __ext_category,
        __vlan_name.name() : __vlan_name,
        __vlan_num.name() : __vlan_num
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 277, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_31_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 280, 46)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 280, 46)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 286, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_32_category', pyxb.binding.datatypes.string)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 289, 46)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 289, 46)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext_category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_category'), 'ext_category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_32_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 290, 46)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 290, 46)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_32_lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 291, 46)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 291, 46)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __category.name() : __category,
        __ext_category.name() : __ext_category,
        __lang.name() : __lang
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 300, 34)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Port uses Python identifier Port
    __Port = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Port'), 'Port', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_33_urnietfparamsxmlnsiodef_1_0Port', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 302, 38), )

    
    Port = property(__Port.value, __Port.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Portlist uses Python identifier Portlist
    __Portlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Portlist'), 'Portlist', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_33_urnietfparamsxmlnsiodef_1_0Portlist', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 303, 38), )

    
    Portlist = property(__Portlist.value, __Portlist.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ProtoType uses Python identifier ProtoType
    __ProtoType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoType'), 'ProtoType', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_33_urnietfparamsxmlnsiodef_1_0ProtoType', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 304, 38), )

    
    ProtoType = property(__ProtoType.value, __ProtoType.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ProtoCode uses Python identifier ProtoCode
    __ProtoCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode'), 'ProtoCode', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_33_urnietfparamsxmlnsiodef_1_0ProtoCode', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 305, 38), )

    
    ProtoCode = property(__ProtoCode.value, __ProtoCode.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ProtoField uses Python identifier ProtoField
    __ProtoField = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoField'), 'ProtoField', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_33_urnietfparamsxmlnsiodef_1_0ProtoField', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 306, 38), )

    
    ProtoField = property(__ProtoField.value, __ProtoField.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_33_urnietfparamsxmlnsiodef_1_0Application', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 307, 38), )

    
    Application = property(__Application.value, __Application.set, None, None)

    
    # Attribute ip_protocol uses Python identifier ip_protocol
    __ip_protocol = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ip_protocol'), 'ip_protocol', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_33_ip_protocol', pyxb.binding.datatypes.string)
    __ip_protocol._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 322, 36)
    __ip_protocol._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 322, 36)
    
    ip_protocol = property(__ip_protocol.value, __ip_protocol.set, None, None)

    _ElementMap.update({
        __Port.name() : __Port,
        __Portlist.name() : __Portlist,
        __ProtoType.name() : __ProtoType,
        __ProtoCode.name() : __ProtoCode,
        __ProtoField.name() : __ProtoField,
        __Application.name() : __Application
    })
    _AttributeMap.update({
        __ip_protocol.name() : __ip_protocol
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 308, 40)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_urnietfparamsxmlnsiodef_1_0URL', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 310, 44), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute swid uses Python identifier swid
    __swid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'swid'), 'swid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_swid', pyxb.binding.datatypes.string)
    __swid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 312, 42)
    __swid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 312, 42)
    
    swid = property(__swid.value, __swid.set, None, None)

    
    # Attribute configid uses Python identifier configid
    __configid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'configid'), 'configid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_configid', pyxb.binding.datatypes.string)
    __configid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 313, 42)
    __configid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 313, 42)
    
    configid = property(__configid.value, __configid.set, None, None)

    
    # Attribute vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vendor'), 'vendor', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_vendor', pyxb.binding.datatypes.string)
    __vendor._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 314, 42)
    __vendor._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 314, 42)
    
    vendor = property(__vendor.value, __vendor.set, None, None)

    
    # Attribute family uses Python identifier family
    __family = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'family'), 'family', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_family', pyxb.binding.datatypes.string)
    __family._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 315, 42)
    __family._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 315, 42)
    
    family = property(__family.value, __family.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 316, 42)
    __name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 316, 42)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 317, 42)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 317, 42)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute patch uses Python identifier patch
    __patch = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'patch'), 'patch', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_34_patch', pyxb.binding.datatypes.string)
    __patch._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 318, 42)
    __patch._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 318, 42)
    
    patch = property(__patch.value, __patch.set, None, None)

    _ElementMap.update({
        __URL.name() : __URL
    })
    _AttributeMap.update({
        __swid.name() : __swid,
        __configid.name() : __configid,
        __vendor.name() : __vendor,
        __family.name() : __family,
        __name.name() : __name,
        __version.name() : __version,
        __patch.name() : __patch
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 326, 34)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_urnietfparamsxmlnsiodef_1_0URL', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 328, 38), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute swid uses Python identifier swid
    __swid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'swid'), 'swid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_swid', pyxb.binding.datatypes.string)
    __swid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 330, 36)
    __swid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 330, 36)
    
    swid = property(__swid.value, __swid.set, None, None)

    
    # Attribute configid uses Python identifier configid
    __configid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'configid'), 'configid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_configid', pyxb.binding.datatypes.string)
    __configid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 331, 36)
    __configid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 331, 36)
    
    configid = property(__configid.value, __configid.set, None, None)

    
    # Attribute vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vendor'), 'vendor', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_vendor', pyxb.binding.datatypes.string)
    __vendor._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 332, 36)
    __vendor._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 332, 36)
    
    vendor = property(__vendor.value, __vendor.set, None, None)

    
    # Attribute family uses Python identifier family
    __family = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'family'), 'family', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_family', pyxb.binding.datatypes.string)
    __family._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 333, 36)
    __family._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 333, 36)
    
    family = property(__family.value, __family.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 334, 36)
    __name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 334, 36)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 335, 36)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 335, 36)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute patch uses Python identifier patch
    __patch = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'patch'), 'patch', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_35_patch', pyxb.binding.datatypes.string)
    __patch._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 336, 36)
    __patch._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 336, 36)
    
    patch = property(__patch.value, __patch.set, None, None)

    _ElementMap.update({
        __URL.name() : __URL
    })
    _AttributeMap.update({
        __swid.name() : __swid,
        __configid.name() : __configid,
        __vendor.name() : __vendor,
        __family.name() : __family,
        __name.name() : __name,
        __version.name() : __version,
        __patch.name() : __patch
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 351, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_36_urnietfparamsxmlnsiodef_1_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 353, 26), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_36_urnietfparamsxmlnsiodef_1_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 354, 26), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_36_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 356, 24)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 356, 24)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_36_severity', pyxb.binding.datatypes.string)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 357, 24)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 357, 24)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_36_action', pyxb.binding.datatypes.string)
    __action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 358, 24)
    __action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 358, 24)
    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute ext_action uses Python identifier ext_action
    __ext_action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_action'), 'ext_action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_36_ext_action', pyxb.binding.datatypes.string)
    __ext_action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 359, 24)
    __ext_action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 359, 24)
    
    ext_action = property(__ext_action.value, __ext_action.set, None, None)

    _ElementMap.update({
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __severity.name() : __severity,
        __action.name() : __action,
        __ext_action.name() : __ext_action
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 363, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RecordData uses Python identifier RecordData
    __RecordData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), 'RecordData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_37_urnietfparamsxmlnsiodef_1_0RecordData', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 365, 26), )

    
    RecordData = property(__RecordData.value, __RecordData.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_37_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 401, 24)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 401, 24)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __RecordData.name() : __RecordData
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 366, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_38_urnietfparamsxmlnsiodef_1_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 368, 32), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RecordPattern uses Python identifier RecordPattern
    __RecordPattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), 'RecordPattern', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_38_urnietfparamsxmlnsiodef_1_0RecordPattern', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 369, 32), )

    
    RecordPattern = property(__RecordPattern.value, __RecordPattern.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RecordItem uses Python identifier RecordItem
    __RecordItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), 'RecordItem', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_38_urnietfparamsxmlnsiodef_1_0RecordItem', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 383, 32), )

    
    RecordItem = property(__RecordItem.value, __RecordItem.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_38_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 397, 30)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 397, 30)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __DateTime.name() : __DateTime,
        __RecordPattern.name() : __RecordPattern,
        __RecordItem.name() : __RecordItem
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 370, 34)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_39_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 373, 40)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 373, 40)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext_type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_39_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 374, 40)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 374, 40)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'offset'), 'offset', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_39_offset', pyxb.binding.datatypes.string)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 375, 40)
    __offset._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 375, 40)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute offsetunit uses Python identifier offsetunit
    __offsetunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'offsetunit'), 'offsetunit', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_39_offsetunit', pyxb.binding.datatypes.string)
    __offsetunit._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 376, 40)
    __offsetunit._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 376, 40)
    
    offsetunit = property(__offsetunit.value, __offsetunit.set, None, None)

    
    # Attribute ext_offsetunit uses Python identifier ext_offsetunit
    __ext_offsetunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_offsetunit'), 'ext_offsetunit', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_39_ext_offsetunit', pyxb.binding.datatypes.string)
    __ext_offsetunit._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 377, 40)
    __ext_offsetunit._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 377, 40)
    
    ext_offsetunit = property(__ext_offsetunit.value, __ext_offsetunit.set, None, None)

    
    # Attribute instance uses Python identifier instance
    __instance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instance'), 'instance', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_39_instance', pyxb.binding.datatypes.string)
    __instance._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 378, 40)
    __instance._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 378, 40)
    
    instance = property(__instance.value, __instance.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __ext_type.name() : __ext_type,
        __offset.name() : __offset,
        __offsetunit.name() : __offsetunit,
        __ext_offsetunit.name() : __ext_offsetunit,
        __instance.name() : __instance
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 384, 34)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute dtype uses Python identifier dtype
    __dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dtype'), 'dtype', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_40_dtype', pyxb.binding.datatypes.string)
    __dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 387, 40)
    __dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 387, 40)
    
    dtype = property(__dtype.value, __dtype.set, None, None)

    
    # Attribute ext_dtype uses Python identifier ext_dtype
    __ext_dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_dtype'), 'ext_dtype', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_40_ext_dtype', pyxb.binding.datatypes.string)
    __ext_dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 388, 40)
    __ext_dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 388, 40)
    
    ext_dtype = property(__ext_dtype.value, __ext_dtype.set, None, None)

    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_40_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 389, 40)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 389, 40)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute formatid uses Python identifier formatid
    __formatid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatid'), 'formatid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_40_formatid', pyxb.binding.datatypes.string)
    __formatid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 390, 40)
    __formatid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 390, 40)
    
    formatid = property(__formatid.value, __formatid.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_40_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 391, 40)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 391, 40)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __dtype.name() : __dtype,
        __ext_dtype.name() : __ext_dtype,
        __meaning.name() : __meaning,
        __formatid.name() : __formatid,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 409, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}HistoryItem uses Python identifier HistoryItem
    __HistoryItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), 'HistoryItem', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_41_urnietfparamsxmlnsiodef_1_0HistoryItem', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 411, 20), )

    
    HistoryItem = property(__HistoryItem.value, __HistoryItem.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_41_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 422, 18)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 422, 18)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __HistoryItem.name() : __HistoryItem
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 412, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_42_urnietfparamsxmlnsiodef_1_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 414, 26), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_42_restriction', pyxb.binding.datatypes.string)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 416, 24)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 416, 24)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_42_action', pyxb.binding.datatypes.string)
    __action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 417, 24)
    __action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 417, 24)
    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute ext_action uses Python identifier ext_action
    __ext_action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext_action'), 'ext_action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_42_ext_action', pyxb.binding.datatypes.string)
    __ext_action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 418, 24)
    __ext_action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 418, 24)
    
    ext_action = property(__ext_action.value, __ext_action.set, None, None)

    _ElementMap.update({
        __DateTime.name() : __DateTime
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __action.name() : __action,
        __ext_action.name() : __ext_action
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 439, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_43_urnietfparamsxmlnsiodef_1_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_43_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 14, 2), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IODEF_Document uses Python identifier IODEF_Document
    __IODEF_Document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IODEF_Document'), 'IODEF_Document', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_43_urnietfparamsxmlnsiodef_1_0IODEF_Document', True, pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 32, 2), )

    
    IODEF_Document = property(__IODEF_Document.value, __IODEF_Document.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID,
        __Description.name() : __Description,
        __IODEF_Document.name() : __IODEF_Document
    })
    _AttributeMap.update({
        
    })



IncidentID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), CTD_ANON, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', IncidentID.name().localName(), IncidentID)

Description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), CTD_ANON_, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 14, 2))
Namespace.addCategoryObject('elementBinding', Description.name().localName(), Description)

iodef_sci = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iodef_sci'), CTD_ANON_2, nillable=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 23, 2))
Namespace.addCategoryObject('elementBinding', iodef_sci.name().localName(), iodef_sci)

IODEF_Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IODEF_Document'), CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 32, 2))
Namespace.addCategoryObject('elementBinding', IODEF_Document.name().localName(), IODEF_Document)

NewDataSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NewDataSet'), CTD_ANON_43, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 438, 2))
Namespace.addCategoryObject('elementBinding', NewDataSet.name().localName(), NewDataSet)



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Incident'), CTD_ANON_4, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 35, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 35, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Incident')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 35, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), CTD_ANON, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), CTD_ANON_, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 14, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 38, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 39, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 40, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 41, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 43, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), CTD_ANON_6, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 51, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_7, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 60, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Method'), CTD_ANON_14, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 139, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_18, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 170, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_25, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 238, 14)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'History'), CTD_ANON_41, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 408, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 38, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 39, 14))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 40, 14))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 41, 14))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 42, 14))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 43, 14))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 51, 14))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 59, 14))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 60, 14))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 139, 14))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 170, 14))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 238, 14))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 408, 14))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 38, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 39, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 40, 14))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReportTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 41, 14))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 42, 14))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 43, 14))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 51, 14))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 59, 14))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Assessment')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 60, 14))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Method')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 139, 14))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 170, 14))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventData')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 238, 14))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'History')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 408, 14))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), CTD_ANON, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 46, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 46, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_2()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), CTD_ANON, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 54, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 54, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_3()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Impact'), CTD_ANON_8, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 63, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), CTD_ANON_9, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 76, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), CTD_ANON_10, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 89, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_11, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 99, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), CTD_ANON_12, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 112, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), CTD_ANON_13, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 121, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 63, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 76, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 89, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 99, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 112, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 121, 20))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Impact')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 63, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 76, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 89, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 99, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Confidence')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 112, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 121, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_4()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), CTD_ANON_, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 14, 2)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), CTD_ANON_15, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 142, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 142, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 165, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 142, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 165, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_5()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceName'), CTD_ANON_16, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 145, 26)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), CTD_ANON_17, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 154, 26)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 145, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 154, 26))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceName')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 145, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 154, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_6()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 173, 20)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), CTD_ANON_19, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 174, 20)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), CTD_ANON_20, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 183, 20)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), CTD_ANON_21, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 193, 20)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Email'), CTD_ANON_22, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 203, 20)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), CTD_ANON_23, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 212, 20)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), CTD_ANON_24, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 221, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 173, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 174, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 183, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 193, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 203, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 212, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 221, 20))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Timezone')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 173, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactName')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 174, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 183, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 193, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Email')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 203, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telephone')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 212, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fax')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 221, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_7()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 241, 20)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 242, 20)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 243, 20)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flow'), CTD_ANON_26, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 244, 20)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), CTD_ANON_36, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 350, 20)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Record'), CTD_ANON_37, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 362, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 241, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 242, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 243, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 244, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 350, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 362, 20))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 241, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 242, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 243, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flow')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 244, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Expectation')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 350, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Record')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 362, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_8()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'System'), CTD_ANON_27, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 247, 26)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 247, 26))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'System')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 247, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_9()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Node'), CTD_ANON_28, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 250, 32)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Service'), CTD_ANON_33, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 299, 32)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), CTD_ANON_35, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 325, 32)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 250, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 299, 32))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 325, 32))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Node')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 250, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Service')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 299, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 325, 32))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_10()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 253, 38)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 254, 38)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeName'), CTD_ANON_29, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 255, 38)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), CTD_ANON_30, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 264, 38)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), CTD_ANON_31, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 276, 38)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), CTD_ANON_32, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 285, 38)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 253, 38))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 254, 38))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 255, 38))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 264, 38))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 276, 38))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 285, 38))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 253, 38))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 254, 38))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NodeName')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 255, 38))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 264, 38))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Location')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 276, 38))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NodeRole')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 285, 38))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_11()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Port'), pyxb.binding.datatypes.string, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 302, 38)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Portlist'), pyxb.binding.datatypes.string, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 303, 38)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoType'), pyxb.binding.datatypes.string, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 304, 38)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 305, 38)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoField'), pyxb.binding.datatypes.string, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 306, 38)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), CTD_ANON_34, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 307, 38)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 302, 38))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 303, 38))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 304, 38))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 305, 38))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 306, 38))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 307, 38))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Port')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 302, 38))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Portlist')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 303, 38))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoType')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 304, 38))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 305, 38))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoField')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 306, 38))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 307, 38))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_12()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.string, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 310, 44)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 310, 44))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 310, 44))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_13()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.string, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 328, 38)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 328, 38))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 328, 38))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_14()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 353, 26)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 354, 26)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 353, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 354, 26))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 353, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 354, 26))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_15()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), CTD_ANON_38, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 365, 26)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 365, 26))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordData')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 365, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_16()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 368, 32)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), CTD_ANON_39, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 369, 32)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), CTD_ANON_40, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_38, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 383, 32)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 368, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 369, 32))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 383, 32))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 368, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 369, 32))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordItem')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 383, 32))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_17()




CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), CTD_ANON_42, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 411, 20)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 411, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 411, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_18()




CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.string, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 414, 26)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 414, 26))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 414, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_42._Automaton = _BuildAutomaton_19()




CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), CTD_ANON, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_43, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 3, 2)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), CTD_ANON_, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_43, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 14, 2)))

CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IODEF_Document'), CTD_ANON_3, scope=CTD_ANON_43, location=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 32, 2)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 440, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 441, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 442, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IODEF_Document')), pyxb.utils.utility.Location('/anywhere/iodef-03.xsd', 443, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_43._Automaton = _BuildAutomaton_20()

