# ./iodef-01.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:53f1f331c5e33f9a04da8bb294eb2d0780d80992
# Generated 2014-02-11 12:53:42.573830 by PyXB version 1.2.3
# Namespace urn:ietf:params:xml:ns:iodef-1.0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:19264452-92d0-11e3-b911-001517d2ceb0')

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 70, 10)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.traceback = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'traceback', tag=u'traceback')
STD_ANON.mitigation = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'mitigation', tag=u'mitigation')
STD_ANON.reporting = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'reporting', tag=u'reporting')
STD_ANON.other = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
STD_ANON.ext_value = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 174, 10)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.creator = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'creator', tag=u'creator')
STD_ANON_.admin = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'admin', tag=u'admin')
STD_ANON_.tech = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'tech', tag=u'tech')
STD_ANON_.irt = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'irt', tag=u'irt')
STD_ANON_.cc = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'cc', tag=u'cc')
STD_ANON_.ext_value = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 188, 10)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.person = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'person', tag=u'person')
STD_ANON_2.organization = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'organization', tag=u'organization')
STD_ANON_2.ext_value = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 209, 14)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.internic = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'internic', tag=u'internic')
STD_ANON_3.apnic = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'apnic', tag=u'apnic')
STD_ANON_3.arin = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'arin', tag=u'arin')
STD_ANON_3.lacnic = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'lacnic', tag=u'lacnic')
STD_ANON_3.ripe = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'ripe', tag=u'ripe')
STD_ANON_3.afrinic = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'afrinic', tag=u'afrinic')
STD_ANON_3.local = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'local', tag=u'local')
STD_ANON_3.ext_value = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}TimezoneType
class TimezoneType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TimezoneType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 269, 4)
    _Documentation = None
TimezoneType._CF_pattern = pyxb.binding.facets.CF_pattern()
TimezoneType._CF_pattern.addPattern(pattern=u'Z|[\\+\\-](0[0-9]|1[0-4]):[0-5][0-9]')
TimezoneType._InitializeFacetMap(TimezoneType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TimezoneType', TimezoneType)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 388, 10)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.actual = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'actual', tag=u'actual')
STD_ANON_4.potential = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'potential', tag=u'potential')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 406, 14)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.failed = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'failed', tag=u'failed')
STD_ANON_5.succeeded = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'succeeded', tag=u'succeeded')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 415, 14)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.admin = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'admin', tag=u'admin')
STD_ANON_6.dos = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'dos', tag=u'dos')
STD_ANON_6.extortion = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'extortion', tag=u'extortion')
STD_ANON_6.file = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'file', tag=u'file')
STD_ANON_6.info_leak = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'info-leak', tag=u'info_leak')
STD_ANON_6.misconfiguration = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'misconfiguration', tag=u'misconfiguration')
STD_ANON_6.recon = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'recon', tag=u'recon')
STD_ANON_6.policy = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'policy', tag=u'policy')
STD_ANON_6.social_engineering = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'social-engineering', tag=u'social_engineering')
STD_ANON_6.user = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'user', tag=u'user')
STD_ANON_6.unknown = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_6.ext_value = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 446, 14)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.labor = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'labor', tag=u'labor')
STD_ANON_7.elapsed = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'elapsed', tag=u'elapsed')
STD_ANON_7.downtime = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'downtime', tag=u'downtime')
STD_ANON_7.ext_value = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 480, 10)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.low = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'low', tag=u'low')
STD_ANON_8.medium = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'medium', tag=u'medium')
STD_ANON_8.high = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'high', tag=u'high')
STD_ANON_8.numeric = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'numeric', tag=u'numeric')
STD_ANON_8.unknown = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 567, 10)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.source = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'source', tag=u'source')
STD_ANON_9.target = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'target', tag=u'target')
STD_ANON_9.intermediate = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'intermediate', tag=u'intermediate')
STD_ANON_9.sensor = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'sensor', tag=u'sensor')
STD_ANON_9.infrastructure = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'infrastructure', tag=u'infrastructure')
STD_ANON_9.ext_value = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 582, 10)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.unknown = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_10.yes = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'yes', tag=u'yes')
STD_ANON_10.no = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'no', tag=u'no')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 622, 14)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.asn = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'asn', tag=u'asn')
STD_ANON_11.atm = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'atm', tag=u'atm')
STD_ANON_11.e_mail = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'e-mail', tag=u'e_mail')
STD_ANON_11.mac = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'mac', tag=u'mac')
STD_ANON_11.ipv4_addr = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'ipv4-addr', tag=u'ipv4_addr')
STD_ANON_11.ipv4_net = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'ipv4-net', tag=u'ipv4_net')
STD_ANON_11.ipv4_net_mask = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'ipv4-net-mask', tag=u'ipv4_net_mask')
STD_ANON_11.ipv6_addr = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'ipv6-addr', tag=u'ipv6_addr')
STD_ANON_11.ipv6_net = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'ipv6-net', tag=u'ipv6_net')
STD_ANON_11.ipv6_net_mask = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'ipv6-net-mask', tag=u'ipv6_net_mask')
STD_ANON_11.ext_value = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 654, 14)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.client = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'client', tag=u'client')
STD_ANON_12.server_internal = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'server-internal', tag=u'server_internal')
STD_ANON_12.server_public = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'server-public', tag=u'server_public')
STD_ANON_12.www = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'www', tag=u'www')
STD_ANON_12.mail = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'mail', tag=u'mail')
STD_ANON_12.messaging = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'messaging', tag=u'messaging')
STD_ANON_12.streaming = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'streaming', tag=u'streaming')
STD_ANON_12.voice = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'voice', tag=u'voice')
STD_ANON_12.file = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'file', tag=u'file')
STD_ANON_12.ftp = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'ftp', tag=u'ftp')
STD_ANON_12.p2p = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'p2p', tag=u'p2p')
STD_ANON_12.name = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'name', tag=u'name')
STD_ANON_12.directory = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'directory', tag=u'directory')
STD_ANON_12.credential = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'credential', tag=u'credential')
STD_ANON_12.print_ = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'print', tag=u'print_')
STD_ANON_12.application = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'application', tag=u'application')
STD_ANON_12.database = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'database', tag=u'database')
STD_ANON_12.infra = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'infra', tag=u'infra')
STD_ANON_12.log = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'log', tag=u'log')
STD_ANON_12.ext_value = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}PortlistType
class PortlistType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PortlistType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 712, 4)
    _Documentation = None
PortlistType._CF_pattern = pyxb.binding.facets.CF_pattern()
PortlistType._CF_pattern.addPattern(pattern=u'\\d+(\\-\\d+)?(,\\d+(\\-\\d+)?)*')
PortlistType._InitializeFacetMap(PortlistType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'PortlistType', PortlistType)

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 727, 14)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.byte = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
STD_ANON_13.packet = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'packet', tag=u'packet')
STD_ANON_13.flow = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'flow', tag=u'flow')
STD_ANON_13.session = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'session', tag=u'session')
STD_ANON_13.event = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'event', tag=u'event')
STD_ANON_13.alert = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'alert', tag=u'alert')
STD_ANON_13.message = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'message', tag=u'message')
STD_ANON_13.host = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'host', tag=u'host')
STD_ANON_13.site = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'site', tag=u'site')
STD_ANON_13.organization = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'organization', tag=u'organization')
STD_ANON_13.ext_value = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 795, 14)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.regex = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'regex', tag=u'regex')
STD_ANON_14.binary = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'binary', tag=u'binary')
STD_ANON_14.xpath = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'xpath', tag=u'xpath')
STD_ANON_14.ext_value = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 810, 14)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.line = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'line', tag=u'line')
STD_ANON_15.byte = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
STD_ANON_15.ext_value = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}PositiveFloatType
class PositiveFloatType (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PositiveFloatType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 871, 4)
    _Documentation = None
PositiveFloatType._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.float, value=pyxb.binding.datatypes.anySimpleType(u'0'))
PositiveFloatType._InitializeFacetMap(PositiveFloatType._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', u'PositiveFloatType', PositiveFloatType)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}restriction-type
class restriction_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'restriction-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 905, 4)
    _Documentation = None
restriction_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=restriction_type, enum_prefix=None)
restriction_type.default = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'default', tag=u'default')
restriction_type.public = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'public', tag=u'public')
restriction_type.need_to_know = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'need-to-know', tag=u'need_to_know')
restriction_type.private = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'private', tag=u'private')
restriction_type._InitializeFacetMap(restriction_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'restriction-type', restriction_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}severity-type
class severity_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'severity-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 914, 4)
    _Documentation = None
severity_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=severity_type, enum_prefix=None)
severity_type.low = severity_type._CF_enumeration.addEnumeration(unicode_value=u'low', tag=u'low')
severity_type.medium = severity_type._CF_enumeration.addEnumeration(unicode_value=u'medium', tag=u'medium')
severity_type.high = severity_type._CF_enumeration.addEnumeration(unicode_value=u'high', tag=u'high')
severity_type._InitializeFacetMap(severity_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'severity-type', severity_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}duration-type
class duration_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'duration-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 922, 4)
    _Documentation = None
duration_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=duration_type, enum_prefix=None)
duration_type.second = duration_type._CF_enumeration.addEnumeration(unicode_value=u'second', tag=u'second')
duration_type.minute = duration_type._CF_enumeration.addEnumeration(unicode_value=u'minute', tag=u'minute')
duration_type.hour = duration_type._CF_enumeration.addEnumeration(unicode_value=u'hour', tag=u'hour')
duration_type.day = duration_type._CF_enumeration.addEnumeration(unicode_value=u'day', tag=u'day')
duration_type.month = duration_type._CF_enumeration.addEnumeration(unicode_value=u'month', tag=u'month')
duration_type.quarter = duration_type._CF_enumeration.addEnumeration(unicode_value=u'quarter', tag=u'quarter')
duration_type.year = duration_type._CF_enumeration.addEnumeration(unicode_value=u'year', tag=u'year')
duration_type.ext_value = duration_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
duration_type._InitializeFacetMap(duration_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'duration-type', duration_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}action-type
class action_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'action-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 935, 4)
    _Documentation = None
action_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=action_type, enum_prefix=None)
action_type.nothing = action_type._CF_enumeration.addEnumeration(unicode_value=u'nothing', tag=u'nothing')
action_type.contact_source_site = action_type._CF_enumeration.addEnumeration(unicode_value=u'contact-source-site', tag=u'contact_source_site')
action_type.contact_target_site = action_type._CF_enumeration.addEnumeration(unicode_value=u'contact-target-site', tag=u'contact_target_site')
action_type.contact_sender = action_type._CF_enumeration.addEnumeration(unicode_value=u'contact-sender', tag=u'contact_sender')
action_type.investigate = action_type._CF_enumeration.addEnumeration(unicode_value=u'investigate', tag=u'investigate')
action_type.block_host = action_type._CF_enumeration.addEnumeration(unicode_value=u'block-host', tag=u'block_host')
action_type.block_network = action_type._CF_enumeration.addEnumeration(unicode_value=u'block-network', tag=u'block_network')
action_type.block_port = action_type._CF_enumeration.addEnumeration(unicode_value=u'block-port', tag=u'block_port')
action_type.rate_limit_host = action_type._CF_enumeration.addEnumeration(unicode_value=u'rate-limit-host', tag=u'rate_limit_host')
action_type.rate_limit_network = action_type._CF_enumeration.addEnumeration(unicode_value=u'rate-limit-network', tag=u'rate_limit_network')
action_type.rate_limit_port = action_type._CF_enumeration.addEnumeration(unicode_value=u'rate-limit-port', tag=u'rate_limit_port')
action_type.remediate_other = action_type._CF_enumeration.addEnumeration(unicode_value=u'remediate-other', tag=u'remediate_other')
action_type.status_triage = action_type._CF_enumeration.addEnumeration(unicode_value=u'status-triage', tag=u'status_triage')
action_type.status_new_info = action_type._CF_enumeration.addEnumeration(unicode_value=u'status-new-info', tag=u'status_new_info')
action_type.other = action_type._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
action_type.ext_value = action_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
action_type._InitializeFacetMap(action_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'action-type', action_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-1.0}dtype-type
class dtype_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dtype-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 956, 4)
    _Documentation = None
dtype_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dtype_type, enum_prefix=None)
dtype_type.boolean = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'boolean', tag=u'boolean')
dtype_type.byte = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
dtype_type.character = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'character', tag=u'character')
dtype_type.date_time = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'date-time', tag=u'date_time')
dtype_type.integer = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'integer', tag=u'integer')
dtype_type.ntpstamp = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'ntpstamp', tag=u'ntpstamp')
dtype_type.portlist = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'portlist', tag=u'portlist')
dtype_type.real = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'real', tag=u'real')
dtype_type.string = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
dtype_type.file = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'file', tag=u'file')
dtype_type.path = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'path', tag=u'path')
dtype_type.frame = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'frame', tag=u'frame')
dtype_type.packet = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'packet', tag=u'packet')
dtype_type.ipv4_packet = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-packet', tag=u'ipv4_packet')
dtype_type.ipv6_packet = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-packet', tag=u'ipv6_packet')
dtype_type.url = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'url', tag=u'url')
dtype_type.csv = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'csv', tag=u'csv')
dtype_type.winreg = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'winreg', tag=u'winreg')
dtype_type.xml = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'xml', tag=u'xml')
dtype_type.ext_value = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
dtype_type._InitializeFacetMap(dtype_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'dtype-type', dtype_type)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 21, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Incident uses Python identifier Incident
    __Incident = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Incident'), 'Incident', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_urnietfparamsxmlnsiodef_1_0Incident', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 39, 4), )

    
    Incident = property(__Incident.value, __Incident.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_version', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'1.00')
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 26, 8)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 26, 8)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_lang', pyxb.binding.datatypes.language, required=True)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 28, 8)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 28, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute formatid uses Python identifier formatid
    __formatid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatid'), 'formatid', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_formatid', pyxb.binding.datatypes.string)
    __formatid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 30, 8)
    __formatid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 30, 8)
    
    formatid = property(__formatid.value, __formatid.set, None, None)

    _ElementMap.update({
        __Incident.name() : __Incident
    })
    _AttributeMap.update({
        __version.name() : __version,
        __lang.name() : __lang,
        __formatid.name() : __formatid
    })



# Complex type {urn:ietf:params:xml:ns:iodef-1.0}ContactMeansType with content type SIMPLE
class ContactMeansType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-1.0}ContactMeansType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContactMeansType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 243, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_ContactMeansType_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 246, 10)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 246, 10)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meaning.name() : __meaning
    })
Namespace.addCategoryObject('typeBinding', u'ContactMeansType', ContactMeansType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 357, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ReferenceName uses Python identifier ReferenceName
    __ReferenceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReferenceName'), 'ReferenceName', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON__urnietfparamsxmlnsiodef_1_0ReferenceName', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 359, 10), )

    
    ReferenceName = property(__ReferenceName.value, __ReferenceName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON__urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON__urnietfparamsxmlnsiodef_1_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 864, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    _ElementMap.update({
        __ReferenceName.name() : __ReferenceName,
        __Description.name() : __Description,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 535, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}System uses Python identifier System
    __System = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'System'), 'System', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_2_urnietfparamsxmlnsiodef_1_0System', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 547, 4), )

    
    System = property(__System.value, __System.set, None, None)

    _ElementMap.update({
        __System.name() : __System
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 598, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_urnietfparamsxmlnsiodef_1_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 257, 4), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}NodeName uses Python identifier NodeName
    __NodeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'NodeName'), 'NodeName', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_urnietfparamsxmlnsiodef_1_0NodeName', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 601, 12), )

    
    NodeName = property(__NodeName.value, __NodeName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_urnietfparamsxmlnsiodef_1_0Address', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 617, 4), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Location'), 'Location', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_urnietfparamsxmlnsiodef_1_0Location', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 648, 4), )

    
    Location = property(__Location.value, __Location.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}NodeRole uses Python identifier NodeRole
    __NodeRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), 'NodeRole', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_urnietfparamsxmlnsiodef_1_0NodeRole', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 649, 4), )

    
    NodeRole = property(__NodeRole.value, __NodeRole.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_3_urnietfparamsxmlnsiodef_1_0Counter', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 722, 4), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    _ElementMap.update({
        __DateTime.name() : __DateTime,
        __NodeName.name() : __NodeName,
        __Address.name() : __Address,
        __Location.name() : __Location,
        __NodeRole.name() : __NodeRole,
        __Counter.name() : __Counter
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 691, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Port uses Python identifier Port
    __Port = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Port'), 'Port', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0Port', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 694, 12), )

    
    Port = property(__Port.value, __Port.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Portlist uses Python identifier Portlist
    __Portlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Portlist'), 'Portlist', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0Portlist', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 696, 12), )

    
    Portlist = property(__Portlist.value, __Portlist.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ProtoType uses Python identifier ProtoType
    __ProtoType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoType'), 'ProtoType', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0ProtoType', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 699, 10), )

    
    ProtoType = property(__ProtoType.value, __ProtoType.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ProtoCode uses Python identifier ProtoCode
    __ProtoCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode'), 'ProtoCode', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0ProtoCode', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 701, 10), )

    
    ProtoCode = property(__ProtoCode.value, __ProtoCode.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ProtoField uses Python identifier ProtoField
    __ProtoField = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoField'), 'ProtoField', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0ProtoField', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 703, 10), )

    
    ProtoField = property(__ProtoField.value, __ProtoField.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_urnietfparamsxmlnsiodef_1_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 853, 4), )

    
    Application = property(__Application.value, __Application.set, None, None)

    
    # Attribute ip_protocol uses Python identifier ip_protocol
    __ip_protocol = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ip_protocol'), 'ip_protocol', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_4_ip_protocol', pyxb.binding.datatypes.integer, required=True)
    __ip_protocol._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 708, 8)
    __ip_protocol._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 708, 8)
    
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



# Complex type {urn:ietf:params:xml:ns:iodef-1.0}SoftwareType with content type ELEMENT_ONLY
class SoftwareType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-1.0}SoftwareType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SoftwareType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 833, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_urnietfparamsxmlnsiodef_1_0URL', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 864, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute swid uses Python identifier swid
    __swid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'swid'), 'swid', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_swid', pyxb.binding.datatypes.string, unicode_default=u'0')
    __swid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 838, 6)
    __swid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 838, 6)
    
    swid = property(__swid.value, __swid.set, None, None)

    
    # Attribute configid uses Python identifier configid
    __configid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'configid'), 'configid', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_configid', pyxb.binding.datatypes.string, unicode_default=u'0')
    __configid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 840, 6)
    __configid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 840, 6)
    
    configid = property(__configid.value, __configid.set, None, None)

    
    # Attribute vendor uses Python identifier vendor
    __vendor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vendor'), 'vendor', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_vendor', pyxb.binding.datatypes.string)
    __vendor._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 842, 6)
    __vendor._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 842, 6)
    
    vendor = property(__vendor.value, __vendor.set, None, None)

    
    # Attribute family uses Python identifier family
    __family = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'family'), 'family', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_family', pyxb.binding.datatypes.string)
    __family._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 844, 6)
    __family._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 844, 6)
    
    family = property(__family.value, __family.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 846, 6)
    __name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 846, 6)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 848, 6)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 848, 6)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute patch uses Python identifier patch
    __patch = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'patch'), 'patch', '__urnietfparamsxmlnsiodef_1_0_SoftwareType_patch', pyxb.binding.datatypes.string)
    __patch._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 850, 6)
    __patch._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 850, 6)
    
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
Namespace.addCategoryObject('typeBinding', u'SoftwareType', SoftwareType)


# Complex type {urn:ietf:params:xml:ns:iodef-1.0}MLStringType with content type SIMPLE
class MLStringType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-1.0}MLStringType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MLStringType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 876, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_MLStringType_lang', pyxb.binding.datatypes.language)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 879, 10)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 879, 10)
    
    lang = property(__lang.value, __lang.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang
    })
Namespace.addCategoryObject('typeBinding', u'MLStringType', MLStringType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 40, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0IncidentID', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AlternativeID uses Python identifier AlternativeID
    __AlternativeID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), 'AlternativeID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0AlternativeID', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 111, 4), )

    
    AlternativeID = property(__AlternativeID.value, __AlternativeID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RelatedActivity uses Python identifier RelatedActivity
    __RelatedActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), 'RelatedActivity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0RelatedActivity', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 126, 4), )

    
    RelatedActivity = property(__RelatedActivity.value, __RelatedActivity.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ReportTime uses Python identifier ReportTime
    __ReportTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), 'ReportTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0ReportTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 259, 4), )

    
    ReportTime = property(__ReportTime.value, __ReportTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DetectTime uses Python identifier DetectTime
    __DetectTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), 'DetectTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0DetectTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 261, 4), )

    
    DetectTime = property(__DetectTime.value, __DetectTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 263, 4), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 265, 4), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}History uses Python identifier History
    __History = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'History'), 'History', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0History', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 279, 4), )

    
    History = property(__History.value, __History.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Method uses Python identifier Method
    __Method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Method'), 'Method', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0Method', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 342, 4), )

    
    Method = property(__Method.value, __Method.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Assessment uses Python identifier Assessment
    __Assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), 'Assessment', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0Assessment', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 373, 4), )

    
    Assessment = property(__Assessment.value, __Assessment.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EventData uses Python identifier EventData
    __EventData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventData'), 'EventData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0EventData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 497, 4), )

    
    EventData = property(__EventData.value, __EventData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute purpose uses Python identifier purpose
    __purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'purpose'), 'purpose', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_purpose', STD_ANON, required=True)
    __purpose._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 69, 8)
    __purpose._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 69, 8)
    
    purpose = property(__purpose.value, __purpose.set, None, None)

    
    # Attribute ext-purpose uses Python identifier ext_purpose
    __ext_purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-purpose'), 'ext_purpose', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_ext_purpose', pyxb.binding.datatypes.string)
    __ext_purpose._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 80, 8)
    __ext_purpose._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 80, 8)
    
    ext_purpose = property(__ext_purpose.value, __ext_purpose.set, None, None)

    
    # Attribute lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lang'), 'lang', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_lang', pyxb.binding.datatypes.language)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 82, 8)
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 82, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_5_restriction', restriction_type, unicode_default=u'private')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 84, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 84, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID,
        __AlternativeID.name() : __AlternativeID,
        __RelatedActivity.name() : __RelatedActivity,
        __AdditionalData.name() : __AdditionalData,
        __Contact.name() : __Contact,
        __ReportTime.name() : __ReportTime,
        __DetectTime.name() : __DetectTime,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __History.name() : __History,
        __Method.name() : __Method,
        __Assessment.name() : __Assessment,
        __EventData.name() : __EventData,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __purpose.name() : __purpose,
        __ext_purpose.name() : __ext_purpose,
        __lang.name() : __lang,
        __restriction.name() : __restriction
    })



# Complex type {urn:ietf:params:xml:ns:iodef-1.0}IncidentIDType with content type SIMPLE
class IncidentIDType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-1.0}IncidentIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IncidentIDType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 94, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__urnietfparamsxmlnsiodef_1_0_IncidentIDType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 97, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 97, 10)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute instance uses Python identifier instance
    __instance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instance'), 'instance', '__urnietfparamsxmlnsiodef_1_0_IncidentIDType_instance', pyxb.binding.datatypes.string)
    __instance._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 99, 10)
    __instance._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 99, 10)
    
    instance = property(__instance.value, __instance.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_IncidentIDType_restriction', restriction_type, unicode_default=u'public')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 101, 10)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 101, 10)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __instance.name() : __instance,
        __restriction.name() : __restriction
    })
Namespace.addCategoryObject('typeBinding', u'IncidentIDType', IncidentIDType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 112, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_6_urnietfparamsxmlnsiodef_1_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_6_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 117, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 117, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 127, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_urnietfparamsxmlnsiodef_1_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 864, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_7_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 134, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 134, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 150, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}ContactName uses Python identifier ContactName
    __ContactName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), 'ContactName', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0ContactName', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 202, 4), )

    
    ContactName = property(__ContactName.value, __ContactName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RegistryHandle uses Python identifier RegistryHandle
    __RegistryHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), 'RegistryHandle', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0RegistryHandle', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 204, 4), )

    
    RegistryHandle = property(__RegistryHandle.value, __RegistryHandle.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}PostalAddress uses Python identifier PostalAddress
    __PostalAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), 'PostalAddress', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0PostalAddress', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 229, 4), )

    
    PostalAddress = property(__PostalAddress.value, __PostalAddress.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Email'), 'Email', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0Email', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 239, 4), )

    
    Email = property(__Email.value, __Email.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Telephone uses Python identifier Telephone
    __Telephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), 'Telephone', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0Telephone', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 240, 4), )

    
    Telephone = property(__Telephone.value, __Telephone.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Fax uses Python identifier Fax
    __Fax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Fax'), 'Fax', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0Fax', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 241, 4), )

    
    Fax = property(__Fax.value, __Fax.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Timezone uses Python identifier Timezone
    __Timezone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), 'Timezone', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0Timezone', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 267, 4), )

    
    Timezone = property(__Timezone.value, __Timezone.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_role', STD_ANON_, required=True)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 173, 8)
    __role._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 173, 8)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute ext-role uses Python identifier ext_role
    __ext_role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-role'), 'ext_role', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_ext_role', pyxb.binding.datatypes.string)
    __ext_role._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 185, 8)
    __ext_role._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 185, 8)
    
    ext_role = property(__ext_role.value, __ext_role.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_type', STD_ANON_2, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 187, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 187, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 196, 8)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 196, 8)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_8_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 198, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 198, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Contact.name() : __Contact,
        __ContactName.name() : __ContactName,
        __RegistryHandle.name() : __RegistryHandle,
        __PostalAddress.name() : __PostalAddress,
        __Email.name() : __Email,
        __Telephone.name() : __Telephone,
        __Fax.name() : __Fax,
        __Timezone.name() : __Timezone,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __role.name() : __role,
        __ext_role.name() : __ext_role,
        __type.name() : __type,
        __ext_type.name() : __ext_type,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 205, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute registry uses Python identifier registry
    __registry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'registry'), 'registry', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_9_registry', STD_ANON_3)
    __registry._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 208, 12)
    __registry._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 208, 12)
    
    registry = property(__registry.value, __registry.set, None, None)

    
    # Attribute ext-registry uses Python identifier ext_registry
    __ext_registry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-registry'), 'ext_registry', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_9_ext_registry', pyxb.binding.datatypes.string)
    __ext_registry._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 222, 12)
    __ext_registry._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 222, 12)
    
    ext_registry = property(__ext_registry.value, __ext_registry.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __registry.name() : __registry,
        __ext_registry.name() : __ext_registry
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_10 (MLStringType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 230, 6)
    _ElementMap = MLStringType._ElementMap.copy()
    _AttributeMap = MLStringType._AttributeMap.copy()
    # Base type is MLStringType
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_10_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 233, 12)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 233, 12)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute lang inherited from {urn:ietf:params:xml:ns:iodef-1.0}MLStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meaning.name() : __meaning
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 280, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}HistoryItem uses Python identifier HistoryItem
    __HistoryItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), 'HistoryItem', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_11_urnietfparamsxmlnsiodef_1_0HistoryItem', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 289, 4), )

    
    HistoryItem = property(__HistoryItem.value, __HistoryItem.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_11_restriction', restriction_type, unicode_default=u'default')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 285, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 285, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __HistoryItem.name() : __HistoryItem
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 290, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_urnietfparamsxmlnsiodef_1_0IncidentID', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_urnietfparamsxmlnsiodef_1_0Contact', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_urnietfparamsxmlnsiodef_1_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 257, 4), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 302, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 302, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_action', action_type, required=True)
    __action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 304, 8)
    __action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 304, 8)
    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute ext-action uses Python identifier ext_action
    __ext_action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-action'), 'ext_action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_12_ext_action', pyxb.binding.datatypes.string)
    __ext_action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 306, 8)
    __ext_action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 306, 8)
    
    ext_action = property(__ext_action.value, __ext_action.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID,
        __AdditionalData.name() : __AdditionalData,
        __Contact.name() : __Contact,
        __DateTime.name() : __DateTime,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __action.name() : __action,
        __ext_action.name() : __ext_action
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 316, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_urnietfparamsxmlnsiodef_1_0Contact', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_urnietfparamsxmlnsiodef_1_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 263, 4), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_urnietfparamsxmlnsiodef_1_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 265, 4), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_restriction', restriction_type, unicode_default=u'default')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 327, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 327, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 329, 8)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 329, 8)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_action', action_type, unicode_default=u'other')
    __action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 331, 8)
    __action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 331, 8)
    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute ext-action uses Python identifier ext_action
    __ext_action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-action'), 'ext_action', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_13_ext_action', pyxb.binding.datatypes.string)
    __ext_action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 333, 8)
    __ext_action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 333, 8)
    
    ext_action = property(__ext_action.value, __ext_action.set, None, None)

    _ElementMap.update({
        __Contact.name() : __Contact,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __severity.name() : __severity,
        __action.name() : __action,
        __ext_action.name() : __ext_action
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 343, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_14_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_14_urnietfparamsxmlnsiodef_1_0Reference', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 356, 4), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_14_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_14_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 352, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 352, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Reference.name() : __Reference,
        __Description.name() : __Description
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
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 374, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Impact uses Python identifier Impact
    __Impact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Impact'), 'Impact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0Impact', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 399, 4), )

    
    Impact = property(__Impact.value, __Impact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}TimeImpact uses Python identifier TimeImpact
    __TimeImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), 'TimeImpact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0TimeImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 438, 4), )

    
    TimeImpact = property(__TimeImpact.value, __TimeImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}MonetaryImpact uses Python identifier MonetaryImpact
    __MonetaryImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), 'MonetaryImpact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0MonetaryImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 465, 4), )

    
    MonetaryImpact = property(__MonetaryImpact.value, __MonetaryImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Confidence uses Python identifier Confidence
    __Confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), 'Confidence', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0Confidence', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 477, 4), )

    
    Confidence = property(__Confidence.value, __Confidence.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_urnietfparamsxmlnsiodef_1_0Counter', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 722, 4), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    
    # Attribute occurrence uses Python identifier occurrence
    __occurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'occurrence'), 'occurrence', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_occurrence', STD_ANON_4)
    __occurrence._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 387, 8)
    __occurrence._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 387, 8)
    
    occurrence = property(__occurrence.value, __occurrence.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_15_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 395, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 395, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Impact.name() : __Impact,
        __TimeImpact.name() : __TimeImpact,
        __MonetaryImpact.name() : __MonetaryImpact,
        __Confidence.name() : __Confidence,
        __Counter.name() : __Counter
    })
    _AttributeMap.update({
        __occurrence.name() : __occurrence,
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_16 (MLStringType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 400, 6)
    _ElementMap = MLStringType._ElementMap.copy()
    _AttributeMap = MLStringType._AttributeMap.copy()
    # Base type is MLStringType
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_16_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 403, 12)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 403, 12)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute completion uses Python identifier completion
    __completion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'completion'), 'completion', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_16_completion', STD_ANON_5)
    __completion._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 405, 12)
    __completion._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 405, 12)
    
    completion = property(__completion.value, __completion.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_16_type', STD_ANON_6, unicode_default=u'unknown')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 413, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 413, 12)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_16_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 432, 12)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 432, 12)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute lang inherited from {urn:ietf:params:xml:ns:iodef-1.0}MLStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __completion.name() : __completion,
        __type.name() : __type,
        __ext_type.name() : __ext_type
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = PositiveFloatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 439, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is PositiveFloatType
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_17_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 442, 12)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 442, 12)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute metric uses Python identifier metric
    __metric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'metric'), 'metric', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_17_metric', STD_ANON_7, required=True)
    __metric._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 444, 12)
    __metric._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 444, 12)
    
    metric = property(__metric.value, __metric.set, None, None)

    
    # Attribute ext-metric uses Python identifier ext_metric
    __ext_metric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-metric'), 'ext_metric', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_17_ext_metric', pyxb.binding.datatypes.string)
    __ext_metric._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 455, 12)
    __ext_metric._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 455, 12)
    
    ext_metric = property(__ext_metric.value, __ext_metric.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_17_duration', duration_type)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 457, 12)
    __duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 457, 12)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute ext-duration uses Python identifier ext_duration
    __ext_duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-duration'), 'ext_duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_17_ext_duration', pyxb.binding.datatypes.string)
    __ext_duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 459, 12)
    __ext_duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 459, 12)
    
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
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = PositiveFloatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 466, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is PositiveFloatType
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 469, 12)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 469, 12)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'currency'), 'currency', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_18_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 471, 12)
    __currency._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 471, 12)
    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __currency.name() : __currency
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 478, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rating uses Python identifier rating
    __rating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rating'), 'rating', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_19_rating', STD_ANON_8, required=True)
    __rating._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 479, 8)
    __rating._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 479, 8)
    
    rating = property(__rating.value, __rating.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rating.name() : __rating
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 498, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DetectTime uses Python identifier DetectTime
    __DetectTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), 'DetectTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0DetectTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 261, 4), )

    
    DetectTime = property(__DetectTime.value, __DetectTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 263, 4), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 265, 4), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Expectation uses Python identifier Expectation
    __Expectation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), 'Expectation', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0Expectation', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 315, 4), )

    
    Expectation = property(__Expectation.value, __Expectation.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Method uses Python identifier Method
    __Method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Method'), 'Method', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0Method', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 342, 4), )

    
    Method = property(__Method.value, __Method.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Assessment uses Python identifier Assessment
    __Assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), 'Assessment', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0Assessment', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 373, 4), )

    
    Assessment = property(__Assessment.value, __Assessment.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}EventData uses Python identifier EventData
    __EventData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventData'), 'EventData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0EventData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 497, 4), )

    
    EventData = property(__EventData.value, __EventData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Flow uses Python identifier Flow
    __Flow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Flow'), 'Flow', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0Flow', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 534, 4), )

    
    Flow = property(__Flow.value, __Flow.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Record uses Python identifier Record
    __Record = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Record'), 'Record', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0Record', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 760, 4), )

    
    Record = property(__Record.value, __Record.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_20_restriction', restriction_type, unicode_default=u'default')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 525, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 525, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Contact.name() : __Contact,
        __DetectTime.name() : __DetectTime,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __Expectation.name() : __Expectation,
        __Method.name() : __Method,
        __Assessment.name() : __Assessment,
        __EventData.name() : __EventData,
        __Flow.name() : __Flow,
        __Record.name() : __Record,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 548, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Node'), 'Node', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_urnietfparamsxmlnsiodef_1_0Node', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 597, 4), )

    
    Node = property(__Node.value, __Node.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Service'), 'Service', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_urnietfparamsxmlnsiodef_1_0Service', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 690, 4), )

    
    Service = property(__Service.value, __Service.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_urnietfparamsxmlnsiodef_1_0Counter', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 722, 4), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}OperatingSystem uses Python identifier OperatingSystem
    __OperatingSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), 'OperatingSystem', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_urnietfparamsxmlnsiodef_1_0OperatingSystem', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 855, 4), )

    
    OperatingSystem = property(__OperatingSystem.value, __OperatingSystem.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 562, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 562, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute interface uses Python identifier interface
    __interface = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'interface'), 'interface', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_interface', pyxb.binding.datatypes.string)
    __interface._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 564, 8)
    __interface._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 564, 8)
    
    interface = property(__interface.value, __interface.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_category', STD_ANON_9)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 566, 8)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 566, 8)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext-category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-category'), 'ext_category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 578, 8)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 578, 8)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute spoofed uses Python identifier spoofed
    __spoofed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'spoofed'), 'spoofed', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_21_spoofed', STD_ANON_10, unicode_default=u'unknown')
    __spoofed._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 580, 8)
    __spoofed._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 580, 8)
    
    spoofed = property(__spoofed.value, __spoofed.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Node.name() : __Node,
        __Service.name() : __Service,
        __Counter.name() : __Counter,
        __OperatingSystem.name() : __OperatingSystem,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __interface.name() : __interface,
        __category.name() : __category,
        __ext_category.name() : __ext_category,
        __spoofed.name() : __spoofed
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 618, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_22_category', STD_ANON_11, unicode_default=u'ipv4-addr')
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 621, 12)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 621, 12)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext-category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-category'), 'ext_category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_22_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 638, 12)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 638, 12)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute vlan-name uses Python identifier vlan_name
    __vlan_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vlan-name'), 'vlan_name', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_22_vlan_name', pyxb.binding.datatypes.string)
    __vlan_name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 640, 12)
    __vlan_name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 640, 12)
    
    vlan_name = property(__vlan_name.value, __vlan_name.set, None, None)

    
    # Attribute vlan-num uses Python identifier vlan_num
    __vlan_num = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vlan-num'), 'vlan_num', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_22_vlan_num', pyxb.binding.datatypes.integer)
    __vlan_num._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 642, 12)
    __vlan_num._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 642, 12)
    
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
class CTD_ANON_23 (MLStringType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 650, 6)
    _ElementMap = MLStringType._ElementMap.copy()
    _AttributeMap = MLStringType._AttributeMap.copy()
    # Base type is MLStringType
    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_23_category', STD_ANON_12, required=True)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 653, 12)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 653, 12)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext-category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-category'), 'ext_category', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_23_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 679, 12)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 679, 12)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute lang inherited from {urn:ietf:params:xml:ns:iodef-1.0}MLStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __category.name() : __category,
        __ext_category.name() : __ext_category
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 723, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_24_type', STD_ANON_13, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 726, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 726, 12)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_24_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 743, 12)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 743, 12)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_24_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 745, 12)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 745, 12)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_24_duration', duration_type)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 747, 12)
    __duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 747, 12)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute ext-duration uses Python identifier ext_duration
    __ext_duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-duration'), 'ext_duration', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_24_ext_duration', pyxb.binding.datatypes.string)
    __ext_duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 749, 12)
    __ext_duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 749, 12)
    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 761, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RecordData uses Python identifier RecordData
    __RecordData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), 'RecordData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_urnietfparamsxmlnsiodef_1_0RecordData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 770, 4), )

    
    RecordData = property(__RecordData.value, __RecordData.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_25_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 766, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 766, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __RecordData.name() : __RecordData
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
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 771, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_urnietfparamsxmlnsiodef_1_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_urnietfparamsxmlnsiodef_1_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 257, 4), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RecordPattern uses Python identifier RecordPattern
    __RecordPattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), 'RecordPattern', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_urnietfparamsxmlnsiodef_1_0RecordPattern', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 790, 4), )

    
    RecordPattern = property(__RecordPattern.value, __RecordPattern.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}RecordItem uses Python identifier RecordItem
    __RecordItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), 'RecordItem', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_urnietfparamsxmlnsiodef_1_0RecordItem', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 826, 4), )

    
    RecordItem = property(__RecordItem.value, __RecordItem.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_urnietfparamsxmlnsiodef_1_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 853, 4), )

    
    Application = property(__Application.value, __Application.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-1.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_urnietfparamsxmlnsiodef_1_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_26_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 786, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 786, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __DateTime.name() : __DateTime,
        __RecordPattern.name() : __RecordPattern,
        __RecordItem.name() : __RecordItem,
        __Application.name() : __Application,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 791, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_type', STD_ANON_14, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 794, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 794, 12)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 804, 12)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 804, 12)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'offset'), 'offset', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_offset', pyxb.binding.datatypes.integer)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 806, 12)
    __offset._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 806, 12)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute offsetunit uses Python identifier offsetunit
    __offsetunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'offsetunit'), 'offsetunit', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_offsetunit', STD_ANON_15, unicode_default=u'line')
    __offsetunit._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 808, 12)
    __offsetunit._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 808, 12)
    
    offsetunit = property(__offsetunit.value, __offsetunit.set, None, None)

    
    # Attribute ext-offsetunit uses Python identifier ext_offsetunit
    __ext_offsetunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-offsetunit'), 'ext_offsetunit', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_ext_offsetunit', pyxb.binding.datatypes.string)
    __ext_offsetunit._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 818, 12)
    __ext_offsetunit._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 818, 12)
    
    ext_offsetunit = property(__ext_offsetunit.value, __ext_offsetunit.set, None, None)

    
    # Attribute instance uses Python identifier instance
    __instance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instance'), 'instance', '__urnietfparamsxmlnsiodef_1_0_CTD_ANON_27_instance', pyxb.binding.datatypes.integer)
    __instance._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 820, 12)
    __instance._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 820, 12)
    
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



# Complex type {urn:ietf:params:xml:ns:iodef-1.0}ExtensionType with content type MIXED
class ExtensionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-1.0}ExtensionType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExtensionType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 884, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute dtype uses Python identifier dtype
    __dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dtype'), 'dtype', '__urnietfparamsxmlnsiodef_1_0_ExtensionType_dtype', dtype_type, required=True)
    __dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 889, 6)
    __dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 889, 6)
    
    dtype = property(__dtype.value, __dtype.set, None, None)

    
    # Attribute ext-dtype uses Python identifier ext_dtype
    __ext_dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-dtype'), 'ext_dtype', '__urnietfparamsxmlnsiodef_1_0_ExtensionType_ext_dtype', pyxb.binding.datatypes.string)
    __ext_dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 891, 6)
    __ext_dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 891, 6)
    
    ext_dtype = property(__ext_dtype.value, __ext_dtype.set, None, None)

    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_1_0_ExtensionType_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 893, 6)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 893, 6)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute formatid uses Python identifier formatid
    __formatid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatid'), 'formatid', '__urnietfparamsxmlnsiodef_1_0_ExtensionType_formatid', pyxb.binding.datatypes.string)
    __formatid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 895, 6)
    __formatid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 895, 6)
    
    formatid = property(__formatid.value, __formatid.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_1_0_ExtensionType_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 897, 6)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 897, 6)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __dtype.name() : __dtype,
        __ext_dtype.name() : __ext_dtype,
        __meaning.name() : __meaning,
        __formatid.name() : __formatid,
        __restriction.name() : __restriction
    })
Namespace.addCategoryObject('typeBinding', u'ExtensionType', ExtensionType)


DateTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 257, 4))
Namespace.addCategoryObject('elementBinding', DateTime.name().localName(), DateTime)

ReportTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 259, 4))
Namespace.addCategoryObject('elementBinding', ReportTime.name().localName(), ReportTime)

DetectTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 261, 4))
Namespace.addCategoryObject('elementBinding', DetectTime.name().localName(), DetectTime)

StartTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 263, 4))
Namespace.addCategoryObject('elementBinding', StartTime.name().localName(), StartTime)

EndTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 265, 4))
Namespace.addCategoryObject('elementBinding', EndTime.name().localName(), EndTime)

URL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 864, 4))
Namespace.addCategoryObject('elementBinding', URL.name().localName(), URL)

IODEF_Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IODEF-Document'), CTD_ANON, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 20, 4))
Namespace.addCategoryObject('elementBinding', IODEF_Document.name().localName(), IODEF_Document)

ContactName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 202, 4))
Namespace.addCategoryObject('elementBinding', ContactName.name().localName(), ContactName)

Email = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Email'), ContactMeansType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 239, 4))
Namespace.addCategoryObject('elementBinding', Email.name().localName(), Email)

Telephone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), ContactMeansType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 240, 4))
Namespace.addCategoryObject('elementBinding', Telephone.name().localName(), Telephone)

Fax = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), ContactMeansType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 241, 4))
Namespace.addCategoryObject('elementBinding', Fax.name().localName(), Fax)

Timezone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), TimezoneType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 267, 4))
Namespace.addCategoryObject('elementBinding', Timezone.name().localName(), Timezone)

Reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), CTD_ANON_, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 356, 4))
Namespace.addCategoryObject('elementBinding', Reference.name().localName(), Reference)

Flow = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flow'), CTD_ANON_2, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 534, 4))
Namespace.addCategoryObject('elementBinding', Flow.name().localName(), Flow)

Node = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Node'), CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 597, 4))
Namespace.addCategoryObject('elementBinding', Node.name().localName(), Node)

Location = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 648, 4))
Namespace.addCategoryObject('elementBinding', Location.name().localName(), Location)

Service = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Service'), CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 690, 4))
Namespace.addCategoryObject('elementBinding', Service.name().localName(), Service)

Application = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 853, 4))
Namespace.addCategoryObject('elementBinding', Application.name().localName(), Application)

OperatingSystem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 855, 4))
Namespace.addCategoryObject('elementBinding', OperatingSystem.name().localName(), OperatingSystem)

Description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4))
Namespace.addCategoryObject('elementBinding', Description.name().localName(), Description)

Incident = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Incident'), CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 39, 4))
Namespace.addCategoryObject('elementBinding', Incident.name().localName(), Incident)

IncidentID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4))
Namespace.addCategoryObject('elementBinding', IncidentID.name().localName(), IncidentID)

AlternativeID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 111, 4))
Namespace.addCategoryObject('elementBinding', AlternativeID.name().localName(), AlternativeID)

RelatedActivity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 126, 4))
Namespace.addCategoryObject('elementBinding', RelatedActivity.name().localName(), RelatedActivity)

AdditionalData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4))
Namespace.addCategoryObject('elementBinding', AdditionalData.name().localName(), AdditionalData)

Contact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4))
Namespace.addCategoryObject('elementBinding', Contact.name().localName(), Contact)

RegistryHandle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), CTD_ANON_9, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 204, 4))
Namespace.addCategoryObject('elementBinding', RegistryHandle.name().localName(), RegistryHandle)

PostalAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 229, 4))
Namespace.addCategoryObject('elementBinding', PostalAddress.name().localName(), PostalAddress)

History = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'History'), CTD_ANON_11, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 279, 4))
Namespace.addCategoryObject('elementBinding', History.name().localName(), History)

HistoryItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 289, 4))
Namespace.addCategoryObject('elementBinding', HistoryItem.name().localName(), HistoryItem)

Expectation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), CTD_ANON_13, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 315, 4))
Namespace.addCategoryObject('elementBinding', Expectation.name().localName(), Expectation)

Method = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Method'), CTD_ANON_14, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 342, 4))
Namespace.addCategoryObject('elementBinding', Method.name().localName(), Method)

Assessment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 373, 4))
Namespace.addCategoryObject('elementBinding', Assessment.name().localName(), Assessment)

Impact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Impact'), CTD_ANON_16, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 399, 4))
Namespace.addCategoryObject('elementBinding', Impact.name().localName(), Impact)

TimeImpact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), CTD_ANON_17, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 438, 4))
Namespace.addCategoryObject('elementBinding', TimeImpact.name().localName(), TimeImpact)

MonetaryImpact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 465, 4))
Namespace.addCategoryObject('elementBinding', MonetaryImpact.name().localName(), MonetaryImpact)

Confidence = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), CTD_ANON_19, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 477, 4))
Namespace.addCategoryObject('elementBinding', Confidence.name().localName(), Confidence)

EventData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 497, 4))
Namespace.addCategoryObject('elementBinding', EventData.name().localName(), EventData)

System = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'System'), CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 547, 4))
Namespace.addCategoryObject('elementBinding', System.name().localName(), System)

Address = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 617, 4))
Namespace.addCategoryObject('elementBinding', Address.name().localName(), Address)

NodeRole = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), CTD_ANON_23, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 649, 4))
Namespace.addCategoryObject('elementBinding', NodeRole.name().localName(), NodeRole)

Counter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_24, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 722, 4))
Namespace.addCategoryObject('elementBinding', Counter.name().localName(), Counter)

Record = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Record'), CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 760, 4))
Namespace.addCategoryObject('elementBinding', Record.name().localName(), Record)

RecordData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 770, 4))
Namespace.addCategoryObject('elementBinding', RecordData.name().localName(), RecordData)

RecordPattern = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), CTD_ANON_27, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 790, 4))
Namespace.addCategoryObject('elementBinding', RecordPattern.name().localName(), RecordPattern)

RecordItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), ExtensionType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 826, 4))
Namespace.addCategoryObject('elementBinding', RecordItem.name().localName(), RecordItem)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Incident'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 39, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Incident')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 23, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceName'), MLStringType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 359, 10)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 864, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 361, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 363, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceName')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 359, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 361, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 363, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'System'), CTD_ANON_21, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 547, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'System')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 537, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 257, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeName'), MLStringType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 601, 12)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), CTD_ANON_22, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 617, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), MLStringType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 648, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), CTD_ANON_23, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 649, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_24, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 722, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 601, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 603, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 606, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 608, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 610, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 612, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NodeName')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 601, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 603, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Location')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 606, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 608, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NodeRole')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 610, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 612, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
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
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
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
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Port'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 694, 12)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Portlist'), PortlistType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 696, 12)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoType'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 699, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 701, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoField'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 703, 10)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 853, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 693, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 699, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 701, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 703, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 705, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Port')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 694, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Portlist')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 696, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoType')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 699, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 701, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoField')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 703, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 705, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 864, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 835, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 835, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SoftwareType._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), CTD_ANON_6, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 111, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), CTD_ANON_7, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 126, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_8, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 259, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 261, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 263, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 265, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'History'), CTD_ANON_11, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 279, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Method'), CTD_ANON_14, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 342, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_15, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 373, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_20, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 497, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 43, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 45, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 47, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 49, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 51, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 54, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 58, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 62, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 64, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 66, 10))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 42, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 43, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 45, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 47, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 49, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 51, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReportTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 53, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 54, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Assessment')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 56, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Method')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 58, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 60, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 62, 10))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'History')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 64, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 66, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 114, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 864, 4)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 129, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 131, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_8()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_8, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), MLStringType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 202, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 204, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), CTD_ANON_10, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 229, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Email'), ContactMeansType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 239, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), ContactMeansType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 240, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), ContactMeansType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 241, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), TimezoneType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 267, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 152, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 154, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 156, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 158, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 160, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 162, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 164, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 166, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 168, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 170, 10))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactName')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 152, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 154, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 156, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 158, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Email')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 160, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telephone')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 162, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fax')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 164, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Timezone')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 166, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 168, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 170, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_9()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), CTD_ANON_12, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 289, 4)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 282, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_10()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 93, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_8, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 257, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 293, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 295, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 299, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 292, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 293, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 295, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 297, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 299, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_11()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_8, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 263, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 265, 4)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 318, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 320, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 322, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 324, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 318, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 320, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 322, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 324, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_12()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), CTD_ANON_, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 356, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 349, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 346, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 347, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 349, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_13()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Impact'), CTD_ANON_16, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 399, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), CTD_ANON_17, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 438, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), CTD_ANON_18, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 465, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), CTD_ANON_19, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 477, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_24, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 722, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 381, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 383, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 384, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Impact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 377, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 378, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 379, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 381, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Confidence')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 383, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 384, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_14()




def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_15()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_8, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 149, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 261, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 263, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 265, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), CTD_ANON_13, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 315, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Method'), CTD_ANON_14, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 342, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_15, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 373, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_20, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 497, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flow'), CTD_ANON_2, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 534, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Record'), CTD_ANON_25, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 760, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 500, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 502, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 504, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 506, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 508, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 510, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 512, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 514, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 516, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 518, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 520, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 522, 10))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 500, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 502, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 504, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 506, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 508, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Assessment')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 510, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Method')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 512, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flow')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 514, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Expectation')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 516, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Record')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 518, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 520, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 522, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_16()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Node'), CTD_ANON_3, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 597, 4)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Service'), CTD_ANON_4, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 690, 4)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_24, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 722, 4)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), SoftwareType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 855, 4)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 551, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 553, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 555, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 557, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 559, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Node')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 550, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Service')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 551, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 553, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 555, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 557, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 559, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_17()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), CTD_ANON_26, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 770, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 763, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_18()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 143, 4)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 257, 4)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), CTD_ANON_27, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 790, 4)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), ExtensionType, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 826, 4)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 853, 4)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 862, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 773, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 775, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 777, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 779, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 783, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 773, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 775, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 777, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 779, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordItem')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 781, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 783, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_19()




def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 886, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/anywhere/iodef-01.xsd', 886, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExtensionType._Automaton = _BuildAutomaton_20()

