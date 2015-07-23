# ./iodef-bis14.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2ac163bd6186f13215ec89b7670c096ea8c98938
# Generated 2015-07-23 21:40:52.908935 by PyXB version 1.2.3
# Namespace urn:ietf:params:xml:ns:iodef-2.0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:046d041c-3138-11e5-943e-001517d2ceb0')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.xml_
import _enum as _ImportedBinding__enum
import _ds as _ImportedBinding__ds
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'urn:ietf:params:xml:ns:iodef-2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_enum = _ImportedBinding__enum.Namespace
_Namespace_enum.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}incident-purpose-type
class incident_purpose_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'incident-purpose-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 104, 4)
    _Documentation = None
incident_purpose_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=incident_purpose_type, enum_prefix=None)
incident_purpose_type.traceback = incident_purpose_type._CF_enumeration.addEnumeration(unicode_value=u'traceback', tag=u'traceback')
incident_purpose_type.mitigation = incident_purpose_type._CF_enumeration.addEnumeration(unicode_value=u'mitigation', tag=u'mitigation')
incident_purpose_type.reporting = incident_purpose_type._CF_enumeration.addEnumeration(unicode_value=u'reporting', tag=u'reporting')
incident_purpose_type.watch = incident_purpose_type._CF_enumeration.addEnumeration(unicode_value=u'watch', tag=u'watch')
incident_purpose_type.other = incident_purpose_type._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
incident_purpose_type.ext_value = incident_purpose_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
incident_purpose_type._InitializeFacetMap(incident_purpose_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'incident-purpose-type', incident_purpose_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}incident-status-type
class incident_status_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'incident-status-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 115, 4)
    _Documentation = None
incident_status_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=incident_status_type, enum_prefix=None)
incident_status_type.new = incident_status_type._CF_enumeration.addEnumeration(unicode_value=u'new', tag=u'new')
incident_status_type.in_progress = incident_status_type._CF_enumeration.addEnumeration(unicode_value=u'in-progress', tag=u'in_progress')
incident_status_type.forwarded = incident_status_type._CF_enumeration.addEnumeration(unicode_value=u'forwarded', tag=u'forwarded')
incident_status_type.resolved = incident_status_type._CF_enumeration.addEnumeration(unicode_value=u'resolved', tag=u'resolved')
incident_status_type.future = incident_status_type._CF_enumeration.addEnumeration(unicode_value=u'future', tag=u'future')
incident_status_type.ext_value = incident_status_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
incident_status_type._InitializeFacetMap(incident_status_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'incident-status-type', incident_status_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}contact-role-type
class contact_role_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contact-role-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 307, 4)
    _Documentation = None
contact_role_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=contact_role_type, enum_prefix=None)
contact_role_type.creator = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'creator', tag=u'creator')
contact_role_type.reporter = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'reporter', tag=u'reporter')
contact_role_type.admin = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'admin', tag=u'admin')
contact_role_type.tech = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'tech', tag=u'tech')
contact_role_type.provider = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'provider', tag=u'provider')
contact_role_type.zone = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'zone', tag=u'zone')
contact_role_type.user = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'user', tag=u'user')
contact_role_type.billing = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'billing', tag=u'billing')
contact_role_type.legal = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'legal', tag=u'legal')
contact_role_type.abuse = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'abuse', tag=u'abuse')
contact_role_type.irt = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'irt', tag=u'irt')
contact_role_type.cc = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'cc', tag=u'cc')
contact_role_type.cc_irt = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'cc-irt', tag=u'cc_irt')
contact_role_type.leo = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'leo', tag=u'leo')
contact_role_type.vendor = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'vendor', tag=u'vendor')
contact_role_type.vendor_services = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'vendor-services', tag=u'vendor_services')
contact_role_type.victim = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'victim', tag=u'victim')
contact_role_type.victim_notified = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'victim-notified', tag=u'victim_notified')
contact_role_type.ext_value = contact_role_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
contact_role_type._InitializeFacetMap(contact_role_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'contact-role-type', contact_role_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}contact-type-type
class contact_type_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contact-type-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 331, 4)
    _Documentation = None
contact_type_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=contact_type_type, enum_prefix=None)
contact_type_type.person = contact_type_type._CF_enumeration.addEnumeration(unicode_value=u'person', tag=u'person')
contact_type_type.organization = contact_type_type._CF_enumeration.addEnumeration(unicode_value=u'organization', tag=u'organization')
contact_type_type.ext_value = contact_type_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
contact_type_type._InitializeFacetMap(contact_type_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'contact-type-type', contact_type_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}registryhandle-registry-type
class registryhandle_registry_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'registryhandle-registry-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 356, 4)
    _Documentation = None
registryhandle_registry_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=registryhandle_registry_type, enum_prefix=None)
registryhandle_registry_type.internic = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'internic', tag=u'internic')
registryhandle_registry_type.apnic = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'apnic', tag=u'apnic')
registryhandle_registry_type.arin = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'arin', tag=u'arin')
registryhandle_registry_type.lacnic = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'lacnic', tag=u'lacnic')
registryhandle_registry_type.ripe = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'ripe', tag=u'ripe')
registryhandle_registry_type.afrinic = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'afrinic', tag=u'afrinic')
registryhandle_registry_type.local = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'local', tag=u'local')
registryhandle_registry_type.ext_value = registryhandle_registry_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
registryhandle_registry_type._InitializeFacetMap(registryhandle_registry_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'registryhandle-registry-type', registryhandle_registry_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}TimezoneType
class TimezoneType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TimezoneType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 413, 4)
    _Documentation = None
TimezoneType._CF_pattern = pyxb.binding.facets.CF_pattern()
TimezoneType._CF_pattern.addPattern(pattern=u'Z|[\\+\\-](0[0-9]|1[0-4]):[0-5][0-9]')
TimezoneType._InitializeFacetMap(TimezoneType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TimezoneType', TimezoneType)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}discovery-source-type
class discovery_source_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'discovery-source-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 527, 4)
    _Documentation = None
discovery_source_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=discovery_source_type, enum_prefix=None)
discovery_source_type.nidps = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'nidps', tag=u'nidps')
discovery_source_type.hips = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'hips', tag=u'hips')
discovery_source_type.siem = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'siem', tag=u'siem')
discovery_source_type.av = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'av', tag=u'av')
discovery_source_type.third_party_monitoring = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'third-party-monitoring', tag=u'third_party_monitoring')
discovery_source_type.incident = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'incident', tag=u'incident')
discovery_source_type.os_log = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'os-log', tag=u'os_log')
discovery_source_type.application_log = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'application-log', tag=u'application_log')
discovery_source_type.device_log = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'device-log', tag=u'device_log')
discovery_source_type.network_flow = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'network-flow', tag=u'network_flow')
discovery_source_type.passive_dns = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'passive-dns', tag=u'passive_dns')
discovery_source_type.investigation = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'investigation', tag=u'investigation')
discovery_source_type.audit = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'audit', tag=u'audit')
discovery_source_type.internal_notification = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'internal-notification', tag=u'internal_notification')
discovery_source_type.external_notification = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'external-notification', tag=u'external_notification')
discovery_source_type.leo = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'leo', tag=u'leo')
discovery_source_type.partner = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'partner', tag=u'partner')
discovery_source_type.actor = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'actor', tag=u'actor')
discovery_source_type.unknown = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
discovery_source_type.ext_value = discovery_source_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
discovery_source_type._InitializeFacetMap(discovery_source_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'discovery-source-type', discovery_source_type)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 637, 10)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.actual = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'actual', tag=u'actual')
STD_ANON.potential = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'potential', tag=u'potential')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 668, 14)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.failed = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'failed', tag=u'failed')
STD_ANON_.succeeded = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'succeeded', tag=u'succeeded')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}systemimpact-type-type
class systemimpact_type_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'systemimpact-type-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 685, 4)
    _Documentation = None
systemimpact_type_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=systemimpact_type_type, enum_prefix=None)
systemimpact_type_type.admin = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'admin', tag=u'admin')
systemimpact_type_type.takeover_account = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'takeover-account', tag=u'takeover_account')
systemimpact_type_type.takeover_service = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'takeover-service', tag=u'takeover_service')
systemimpact_type_type.takeover_system = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'takeover-system', tag=u'takeover_system')
systemimpact_type_type.cps_manipulation = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'cps-manipulation', tag=u'cps_manipulation')
systemimpact_type_type.cps_damage = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'cps-damage', tag=u'cps_damage')
systemimpact_type_type.availability_data = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'availability-data', tag=u'availability_data')
systemimpact_type_type.availibility_account = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'availibility-account', tag=u'availibility_account')
systemimpact_type_type.availibility_service = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'availibility-service', tag=u'availibility_service')
systemimpact_type_type.availibility_system = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'availibility-system', tag=u'availibility_system')
systemimpact_type_type.damaged_system = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'damaged-system', tag=u'damaged_system')
systemimpact_type_type.damaged_data = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'damaged-data', tag=u'damaged_data')
systemimpact_type_type.breach_proprietary = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'breach-proprietary', tag=u'breach_proprietary')
systemimpact_type_type.breach_privacy = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'breach-privacy', tag=u'breach_privacy')
systemimpact_type_type.breach_credential = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'breach-credential', tag=u'breach_credential')
systemimpact_type_type.breach_configuration = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'breach-configuration', tag=u'breach_configuration')
systemimpact_type_type.integrity_data = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'integrity-data', tag=u'integrity_data')
systemimpact_type_type.integrity_configuration = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'integrity-configuration', tag=u'integrity_configuration')
systemimpact_type_type.integrity_hardware = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'integrity-hardware', tag=u'integrity_hardware')
systemimpact_type_type.traffic_redirection = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'traffic-redirection', tag=u'traffic_redirection')
systemimpact_type_type.monitoring_traffic = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'monitoring-traffic', tag=u'monitoring_traffic')
systemimpact_type_type.monitoring_host = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'monitoring-host', tag=u'monitoring_host')
systemimpact_type_type.policy = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'policy', tag=u'policy')
systemimpact_type_type.ext_value = systemimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
systemimpact_type_type._InitializeFacetMap(systemimpact_type_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'systemimpact-type-type', systemimpact_type_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}businessimpact-severity-type
class businessimpact_severity_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessimpact-severity-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 731, 4)
    _Documentation = None
businessimpact_severity_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessimpact_severity_type, enum_prefix=None)
businessimpact_severity_type.none = businessimpact_severity_type._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
businessimpact_severity_type.low = businessimpact_severity_type._CF_enumeration.addEnumeration(unicode_value=u'low', tag=u'low')
businessimpact_severity_type.medium = businessimpact_severity_type._CF_enumeration.addEnumeration(unicode_value=u'medium', tag=u'medium')
businessimpact_severity_type.high = businessimpact_severity_type._CF_enumeration.addEnumeration(unicode_value=u'high', tag=u'high')
businessimpact_severity_type.unknown = businessimpact_severity_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
businessimpact_severity_type.ext_value = businessimpact_severity_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
businessimpact_severity_type._InitializeFacetMap(businessimpact_severity_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'businessimpact-severity-type', businessimpact_severity_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}businessimpact-type-type
class businessimpact_type_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessimpact-type-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 742, 4)
    _Documentation = None
businessimpact_type_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessimpact_type_type, enum_prefix=None)
businessimpact_type_type.breach_proprietary = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'breach-proprietary', tag=u'breach_proprietary')
businessimpact_type_type.breach_privacy = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'breach-privacy', tag=u'breach_privacy')
businessimpact_type_type.breach_credential = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'breach-credential', tag=u'breach_credential')
businessimpact_type_type.loss_of_integrity = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'loss-of-integrity', tag=u'loss_of_integrity')
businessimpact_type_type.loss_of_service = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'loss-of-service', tag=u'loss_of_service')
businessimpact_type_type.theft_financial = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'theft-financial', tag=u'theft_financial')
businessimpact_type_type.theft_service = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'theft-service', tag=u'theft_service')
businessimpact_type_type.degraded_reputation = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'degraded-reputation', tag=u'degraded_reputation')
businessimpact_type_type.asset_damage = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'asset-damage', tag=u'asset_damage')
businessimpact_type_type.asset_manipulation = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'asset-manipulation', tag=u'asset_manipulation')
businessimpact_type_type.legal = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'legal', tag=u'legal')
businessimpact_type_type.extortion = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'extortion', tag=u'extortion')
businessimpact_type_type.ext_value = businessimpact_type_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
businessimpact_type_type._InitializeFacetMap(businessimpact_type_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'businessimpact-type-type', businessimpact_type_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}timeimpact-metric-type
class timeimpact_metric_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'timeimpact-metric-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 775, 4)
    _Documentation = None
timeimpact_metric_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=timeimpact_metric_type, enum_prefix=None)
timeimpact_metric_type.labor = timeimpact_metric_type._CF_enumeration.addEnumeration(unicode_value=u'labor', tag=u'labor')
timeimpact_metric_type.elapsed = timeimpact_metric_type._CF_enumeration.addEnumeration(unicode_value=u'elapsed', tag=u'elapsed')
timeimpact_metric_type.downtime = timeimpact_metric_type._CF_enumeration.addEnumeration(unicode_value=u'downtime', tag=u'downtime')
timeimpact_metric_type.ext_value = timeimpact_metric_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
timeimpact_metric_type._InitializeFacetMap(timeimpact_metric_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'timeimpact-metric-type', timeimpact_metric_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}confidence-rating-type
class confidence_rating_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'confidence-rating-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 804, 4)
    _Documentation = None
confidence_rating_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=confidence_rating_type, enum_prefix=None)
confidence_rating_type.low = confidence_rating_type._CF_enumeration.addEnumeration(unicode_value=u'low', tag=u'low')
confidence_rating_type.medium = confidence_rating_type._CF_enumeration.addEnumeration(unicode_value=u'medium', tag=u'medium')
confidence_rating_type.high = confidence_rating_type._CF_enumeration.addEnumeration(unicode_value=u'high', tag=u'high')
confidence_rating_type.numeric = confidence_rating_type._CF_enumeration.addEnumeration(unicode_value=u'numeric', tag=u'numeric')
confidence_rating_type.unknown = confidence_rating_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
confidence_rating_type._InitializeFacetMap(confidence_rating_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'confidence-rating-type', confidence_rating_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}system-category-type
class system_category_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'system-category-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 919, 4)
    _Documentation = None
system_category_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=system_category_type, enum_prefix=None)
system_category_type.source = system_category_type._CF_enumeration.addEnumeration(unicode_value=u'source', tag=u'source')
system_category_type.target = system_category_type._CF_enumeration.addEnumeration(unicode_value=u'target', tag=u'target')
system_category_type.intermediate = system_category_type._CF_enumeration.addEnumeration(unicode_value=u'intermediate', tag=u'intermediate')
system_category_type.sensor = system_category_type._CF_enumeration.addEnumeration(unicode_value=u'sensor', tag=u'sensor')
system_category_type.infrastructure = system_category_type._CF_enumeration.addEnumeration(unicode_value=u'infrastructure', tag=u'infrastructure')
system_category_type.ext_value = system_category_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
system_category_type._InitializeFacetMap(system_category_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'system-category-type', system_category_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}system-ownership-type
class system_ownership_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'system-ownership-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 930, 4)
    _Documentation = None
system_ownership_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=system_ownership_type, enum_prefix=None)
system_ownership_type.organization = system_ownership_type._CF_enumeration.addEnumeration(unicode_value=u'organization', tag=u'organization')
system_ownership_type.personal = system_ownership_type._CF_enumeration.addEnumeration(unicode_value=u'personal', tag=u'personal')
system_ownership_type.partner = system_ownership_type._CF_enumeration.addEnumeration(unicode_value=u'partner', tag=u'partner')
system_ownership_type.customer = system_ownership_type._CF_enumeration.addEnumeration(unicode_value=u'customer', tag=u'customer')
system_ownership_type.no_relationship = system_ownership_type._CF_enumeration.addEnumeration(unicode_value=u'no-relationship', tag=u'no_relationship')
system_ownership_type.unknown = system_ownership_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
system_ownership_type.ext_value = system_ownership_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
system_ownership_type._InitializeFacetMap(system_ownership_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'system-ownership-type', system_ownership_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}address-category-type
class address_category_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'address-category-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 987, 4)
    _Documentation = None
address_category_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=address_category_type, enum_prefix=None)
address_category_type.asn = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'asn', tag=u'asn')
address_category_type.atm = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'atm', tag=u'atm')
address_category_type.e_mail = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'e-mail', tag=u'e_mail')
address_category_type.mac = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'mac', tag=u'mac')
address_category_type.ipv4_addr = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-addr', tag=u'ipv4_addr')
address_category_type.ipv4_net = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-net', tag=u'ipv4_net')
address_category_type.ipv4_net_mask = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-net-mask', tag=u'ipv4_net_mask')
address_category_type.ipv6_addr = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-addr', tag=u'ipv6_addr')
address_category_type.ipv6_net = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-net', tag=u'ipv6_net')
address_category_type.ipv6_net_mask = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-net-mask', tag=u'ipv6_net_mask')
address_category_type.site_uri = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'site-uri', tag=u'site_uri')
address_category_type.ext_value = address_category_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
address_category_type._InitializeFacetMap(address_category_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'address-category-type', address_category_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}noderole-category-type
class noderole_category_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'noderole-category-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1020, 4)
    _Documentation = None
noderole_category_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=noderole_category_type, enum_prefix=None)
noderole_category_type.client = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'client', tag=u'client')
noderole_category_type.client_enterprise = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'client-enterprise', tag=u'client_enterprise')
noderole_category_type.client_partner = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'client-partner', tag=u'client_partner')
noderole_category_type.client_remote = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'client-remote', tag=u'client_remote')
noderole_category_type.client_kiosk = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'client-kiosk', tag=u'client_kiosk')
noderole_category_type.client_mobile = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'client-mobile', tag=u'client_mobile')
noderole_category_type.server_internal = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'server-internal', tag=u'server_internal')
noderole_category_type.server_public = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'server-public', tag=u'server_public')
noderole_category_type.www = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'www', tag=u'www')
noderole_category_type.mail = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'mail', tag=u'mail')
noderole_category_type.webmail = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'webmail', tag=u'webmail')
noderole_category_type.messaging = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'messaging', tag=u'messaging')
noderole_category_type.streaming = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'streaming', tag=u'streaming')
noderole_category_type.voice = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'voice', tag=u'voice')
noderole_category_type.file = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'file', tag=u'file')
noderole_category_type.ftp = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'ftp', tag=u'ftp')
noderole_category_type.p2p = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'p2p', tag=u'p2p')
noderole_category_type.name = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'name', tag=u'name')
noderole_category_type.directory = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'directory', tag=u'directory')
noderole_category_type.credential = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'credential', tag=u'credential')
noderole_category_type.print_ = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'print', tag=u'print_')
noderole_category_type.application = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'application', tag=u'application')
noderole_category_type.database = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'database', tag=u'database')
noderole_category_type.backup = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'backup', tag=u'backup')
noderole_category_type.dhcp = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'dhcp', tag=u'dhcp')
noderole_category_type.assessment = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'assessment', tag=u'assessment')
noderole_category_type.source_control = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'source-control', tag=u'source_control')
noderole_category_type.config_management = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'config-management', tag=u'config_management')
noderole_category_type.monitoring = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'monitoring', tag=u'monitoring')
noderole_category_type.infra = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'infra', tag=u'infra')
noderole_category_type.infra_firewall = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'infra-firewall', tag=u'infra_firewall')
noderole_category_type.infra_router = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'infra-router', tag=u'infra_router')
noderole_category_type.infra_switch = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'infra-switch', tag=u'infra_switch')
noderole_category_type.camera = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'camera', tag=u'camera')
noderole_category_type.proxy = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'proxy', tag=u'proxy')
noderole_category_type.remote_access = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'remote-access', tag=u'remote_access')
noderole_category_type.log = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'log', tag=u'log')
noderole_category_type.virtualization = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'virtualization', tag=u'virtualization')
noderole_category_type.pos = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'pos', tag=u'pos')
noderole_category_type.scada = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'scada', tag=u'scada')
noderole_category_type.scada_supervisory = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'scada-supervisory', tag=u'scada_supervisory')
noderole_category_type.sinkhole = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'sinkhole', tag=u'sinkhole')
noderole_category_type.honeypot = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'honeypot', tag=u'honeypot')
noderole_category_type.anonymization = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'anonymization', tag=u'anonymization')
noderole_category_type.c2_server = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'c2-server', tag=u'c2_server')
noderole_category_type.malware_distribution = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'malware-distribution', tag=u'malware_distribution')
noderole_category_type.drop_server = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'drop-server', tag=u'drop_server')
noderole_category_type.hop_point = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'hop-point', tag=u'hop_point')
noderole_category_type.reflector = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'reflector', tag=u'reflector')
noderole_category_type.phishing_site = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'phishing-site', tag=u'phishing_site')
noderole_category_type.spear_phishing_site = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'spear-phishing-site', tag=u'spear_phishing_site')
noderole_category_type.recruiting_site = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'recruiting-site', tag=u'recruiting_site')
noderole_category_type.fraudulent_site = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'fraudulent-site', tag=u'fraudulent_site')
noderole_category_type.ext_value = noderole_category_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
noderole_category_type._InitializeFacetMap(noderole_category_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'noderole-category-type', noderole_category_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}counter-type-type
class counter_type_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'counter-type-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1159, 4)
    _Documentation = None
counter_type_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=counter_type_type, enum_prefix=None)
counter_type_type.counter = counter_type_type._CF_enumeration.addEnumeration(unicode_value=u'counter', tag=u'counter')
counter_type_type.rate = counter_type_type._CF_enumeration.addEnumeration(unicode_value=u'rate', tag=u'rate')
counter_type_type.average = counter_type_type._CF_enumeration.addEnumeration(unicode_value=u'average', tag=u'average')
counter_type_type.ext_value = counter_type_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
counter_type_type._InitializeFacetMap(counter_type_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'counter-type-type', counter_type_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}counter-unit-type
class counter_unit_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'counter-unit-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1168, 4)
    _Documentation = None
counter_unit_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=counter_unit_type, enum_prefix=None)
counter_unit_type.byte = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
counter_unit_type.mbit = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'mbit', tag=u'mbit')
counter_unit_type.packet = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'packet', tag=u'packet')
counter_unit_type.flow = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'flow', tag=u'flow')
counter_unit_type.session = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'session', tag=u'session')
counter_unit_type.event = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'event', tag=u'event')
counter_unit_type.alert = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'alert', tag=u'alert')
counter_unit_type.message = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'message', tag=u'message')
counter_unit_type.host = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'host', tag=u'host')
counter_unit_type.site = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'site', tag=u'site')
counter_unit_type.organization = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'organization', tag=u'organization')
counter_unit_type.ext_value = counter_unit_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
counter_unit_type._InitializeFacetMap(counter_unit_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'counter-unit-type', counter_unit_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}domaindata-system-status-type
class domaindata_system_status_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'domaindata-system-status-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1253, 2)
    _Documentation = None
domaindata_system_status_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=domaindata_system_status_type, enum_prefix=None)
domaindata_system_status_type.spoofed = domaindata_system_status_type._CF_enumeration.addEnumeration(unicode_value=u'spoofed', tag=u'spoofed')
domaindata_system_status_type.fraudulent = domaindata_system_status_type._CF_enumeration.addEnumeration(unicode_value=u'fraudulent', tag=u'fraudulent')
domaindata_system_status_type.innocent_hacked = domaindata_system_status_type._CF_enumeration.addEnumeration(unicode_value=u'innocent-hacked', tag=u'innocent_hacked')
domaindata_system_status_type.innocent_hijacked = domaindata_system_status_type._CF_enumeration.addEnumeration(unicode_value=u'innocent-hijacked', tag=u'innocent_hijacked')
domaindata_system_status_type.unknown = domaindata_system_status_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
domaindata_system_status_type.ext_value = domaindata_system_status_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
domaindata_system_status_type._InitializeFacetMap(domaindata_system_status_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'domaindata-system-status-type', domaindata_system_status_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}domaindata-domain-status-type
class domaindata_domain_status_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'domaindata-domain-status-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1264, 2)
    _Documentation = None
domaindata_domain_status_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=domaindata_domain_status_type, enum_prefix=None)
domaindata_domain_status_type.reservedDelegation = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'reservedDelegation', tag=u'reservedDelegation')
domaindata_domain_status_type.assignedAndActive = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'assignedAndActive', tag=u'assignedAndActive')
domaindata_domain_status_type.assignedAndInactive = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'assignedAndInactive', tag=u'assignedAndInactive')
domaindata_domain_status_type.assignedAndOnHold = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'assignedAndOnHold', tag=u'assignedAndOnHold')
domaindata_domain_status_type.revoked = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'revoked', tag=u'revoked')
domaindata_domain_status_type.transferPending = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'transferPending', tag=u'transferPending')
domaindata_domain_status_type.registryLock = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'registryLock', tag=u'registryLock')
domaindata_domain_status_type.registrarLock = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'registrarLock', tag=u'registrarLock')
domaindata_domain_status_type.other = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
domaindata_domain_status_type.unknown = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
domaindata_domain_status_type.ext_value = domaindata_domain_status_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
domaindata_domain_status_type._InitializeFacetMap(domaindata_domain_status_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'domaindata-domain-status-type', domaindata_domain_status_type)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1285, 8)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.A = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'A', tag=u'A')
STD_ANON_2.AAAA = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'AAAA', tag=u'AAAA')
STD_ANON_2.AFSDB = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'AFSDB', tag=u'AFSDB')
STD_ANON_2.APL = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'APL', tag=u'APL')
STD_ANON_2.AXFR = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'AXFR', tag=u'AXFR')
STD_ANON_2.CAA = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'CAA', tag=u'CAA')
STD_ANON_2.CERT = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'CERT', tag=u'CERT')
STD_ANON_2.CNAME = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'CNAME', tag=u'CNAME')
STD_ANON_2.DHCID = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'DHCID', tag=u'DHCID')
STD_ANON_2.DLV = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'DLV', tag=u'DLV')
STD_ANON_2.DNAME = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'DNAME', tag=u'DNAME')
STD_ANON_2.DNSKEY = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'DNSKEY', tag=u'DNSKEY')
STD_ANON_2.DS = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'DS', tag=u'DS')
STD_ANON_2.HIP = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'HIP', tag=u'HIP')
STD_ANON_2.IXFR = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'IXFR', tag=u'IXFR')
STD_ANON_2.IPSECKEY = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'IPSECKEY', tag=u'IPSECKEY')
STD_ANON_2.LOC = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'LOC', tag=u'LOC')
STD_ANON_2.MX = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'MX', tag=u'MX')
STD_ANON_2.NAPTR = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'NAPTR', tag=u'NAPTR')
STD_ANON_2.NS = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'NS', tag=u'NS')
STD_ANON_2.NSEC = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'NSEC', tag=u'NSEC')
STD_ANON_2.NSEC3 = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'NSEC3', tag=u'NSEC3')
STD_ANON_2.NSEC3PARAM = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'NSEC3PARAM', tag=u'NSEC3PARAM')
STD_ANON_2.OPT = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'OPT', tag=u'OPT')
STD_ANON_2.PTR = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'PTR', tag=u'PTR')
STD_ANON_2.RRSIG = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'RRSIG', tag=u'RRSIG')
STD_ANON_2.RP = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'RP', tag=u'RP')
STD_ANON_2.SIG = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'SIG', tag=u'SIG')
STD_ANON_2.SOA = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'SOA', tag=u'SOA')
STD_ANON_2.SPF = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'SPF', tag=u'SPF')
STD_ANON_2.SRV = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'SRV', tag=u'SRV')
STD_ANON_2.SSHFP = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'SSHFP', tag=u'SSHFP')
STD_ANON_2.TA = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'TA', tag=u'TA')
STD_ANON_2.TKEY = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'TKEY', tag=u'TKEY')
STD_ANON_2.TLSA = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'TLSA', tag=u'TLSA')
STD_ANON_2.TSIG = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'TSIG', tag=u'TSIG')
STD_ANON_2.TXT = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'TXT', tag=u'TXT')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}recordpattern-type-type
class recordpattern_type_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recordpattern-type-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1426, 4)
    _Documentation = None
recordpattern_type_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=recordpattern_type_type, enum_prefix=None)
recordpattern_type_type.regex = recordpattern_type_type._CF_enumeration.addEnumeration(unicode_value=u'regex', tag=u'regex')
recordpattern_type_type.binary = recordpattern_type_type._CF_enumeration.addEnumeration(unicode_value=u'binary', tag=u'binary')
recordpattern_type_type.xpath = recordpattern_type_type._CF_enumeration.addEnumeration(unicode_value=u'xpath', tag=u'xpath')
recordpattern_type_type.ext_value = recordpattern_type_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
recordpattern_type_type._InitializeFacetMap(recordpattern_type_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'recordpattern-type-type', recordpattern_type_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}recordpattern-offsetunit-type
class recordpattern_offsetunit_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'recordpattern-offsetunit-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1435, 4)
    _Documentation = None
recordpattern_offsetunit_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=recordpattern_offsetunit_type, enum_prefix=None)
recordpattern_offsetunit_type.line = recordpattern_offsetunit_type._CF_enumeration.addEnumeration(unicode_value=u'line', tag=u'line')
recordpattern_offsetunit_type.byte = recordpattern_offsetunit_type._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
recordpattern_offsetunit_type.ext_value = recordpattern_offsetunit_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
recordpattern_offsetunit_type._InitializeFacetMap(recordpattern_offsetunit_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'recordpattern-offsetunit-type', recordpattern_offsetunit_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}key-registryaction-type
class key_registryaction_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'key-registryaction-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1477, 5)
    _Documentation = None
key_registryaction_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=key_registryaction_type, enum_prefix=None)
key_registryaction_type.add_key = key_registryaction_type._CF_enumeration.addEnumeration(unicode_value=u'add-key', tag=u'add_key')
key_registryaction_type.add_value = key_registryaction_type._CF_enumeration.addEnumeration(unicode_value=u'add-value', tag=u'add_value')
key_registryaction_type.delete_key = key_registryaction_type._CF_enumeration.addEnumeration(unicode_value=u'delete-key', tag=u'delete_key')
key_registryaction_type.delete_value = key_registryaction_type._CF_enumeration.addEnumeration(unicode_value=u'delete-value', tag=u'delete_value')
key_registryaction_type.modify_key = key_registryaction_type._CF_enumeration.addEnumeration(unicode_value=u'modify-key', tag=u'modify_key')
key_registryaction_type.modify_value = key_registryaction_type._CF_enumeration.addEnumeration(unicode_value=u'modify-value', tag=u'modify_value')
key_registryaction_type.ext_value = key_registryaction_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
key_registryaction_type._InitializeFacetMap(key_registryaction_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'key-registryaction-type', key_registryaction_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}hashdata-scope-type
class hashdata_scope_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hashdata-scope-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1562, 2)
    _Documentation = None
hashdata_scope_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=hashdata_scope_type, enum_prefix=None)
hashdata_scope_type.file_contents = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'file-contents', tag=u'file_contents')
hashdata_scope_type.file_pe_section = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'file-pe-section', tag=u'file_pe_section')
hashdata_scope_type.file_pe_iat = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'file-pe-iat', tag=u'file_pe_iat')
hashdata_scope_type.file_pe_resource = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'file-pe-resource', tag=u'file_pe_resource')
hashdata_scope_type.file_pdf_object = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'file-pdf-object', tag=u'file_pdf_object')
hashdata_scope_type.email_hash = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'email-hash', tag=u'email_hash')
hashdata_scope_type.email_headers_hash = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'email-headers-hash', tag=u'email_headers_hash')
hashdata_scope_type.email_body_hash = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'email-body-hash', tag=u'email_body_hash')
hashdata_scope_type.ext_value = hashdata_scope_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
hashdata_scope_type._InitializeFacetMap(hashdata_scope_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'hashdata-scope-type', hashdata_scope_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}softwarereference-spec-name-type
class softwarereference_spec_name_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'softwarereference-spec-name-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1679, 4)
    _Documentation = None
softwarereference_spec_name_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=softwarereference_spec_name_type, enum_prefix=None)
softwarereference_spec_name_type.custom = softwarereference_spec_name_type._CF_enumeration.addEnumeration(unicode_value=u'custom', tag=u'custom')
softwarereference_spec_name_type.cpe = softwarereference_spec_name_type._CF_enumeration.addEnumeration(unicode_value=u'cpe', tag=u'cpe')
softwarereference_spec_name_type.swid = softwarereference_spec_name_type._CF_enumeration.addEnumeration(unicode_value=u'swid', tag=u'swid')
softwarereference_spec_name_type.ext_value = softwarereference_spec_name_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
softwarereference_spec_name_type._InitializeFacetMap(softwarereference_spec_name_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'softwarereference-spec-name-type', softwarereference_spec_name_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}softwarereference-dtype-type
class softwarereference_dtype_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'softwarereference-dtype-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1688, 4)
    _Documentation = None
softwarereference_dtype_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=softwarereference_dtype_type, enum_prefix=None)
softwarereference_dtype_type.bytes = softwarereference_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'bytes', tag=u'bytes')
softwarereference_dtype_type.integer = softwarereference_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'integer', tag=u'integer')
softwarereference_dtype_type.real = softwarereference_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'real', tag=u'real')
softwarereference_dtype_type.string = softwarereference_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
softwarereference_dtype_type.xml = softwarereference_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'xml', tag=u'xml')
softwarereference_dtype_type.ext_value = softwarereference_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
softwarereference_dtype_type._InitializeFacetMap(softwarereference_dtype_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'softwarereference-dtype-type', softwarereference_dtype_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}observable-type-type
class observable_type_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'observable-type-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1833, 3)
    _Documentation = None
observable_type_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=observable_type_type, enum_prefix=None)
observable_type_type.asn = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'asn', tag=u'asn')
observable_type_type.atm = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'atm', tag=u'atm')
observable_type_type.e_mail = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'e-mail', tag=u'e_mail')
observable_type_type.ipv4_addr = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-addr', tag=u'ipv4_addr')
observable_type_type.ipv4_net = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-net', tag=u'ipv4_net')
observable_type_type.ipv4_net_mask = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-net-mask', tag=u'ipv4_net_mask')
observable_type_type.ipv6_addr = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-addr', tag=u'ipv6_addr')
observable_type_type.ipv6_net = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-net', tag=u'ipv6_net')
observable_type_type.ipv6_net_mask = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-net-mask', tag=u'ipv6_net_mask')
observable_type_type.mac = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'mac', tag=u'mac')
observable_type_type.site_uri = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'site-uri', tag=u'site_uri')
observable_type_type.fqdn = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'fqdn', tag=u'fqdn')
observable_type_type.doman_name = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'doman-name', tag=u'doman_name')
observable_type_type.domain_to_ipv4 = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'domain-to-ipv4', tag=u'domain_to_ipv4')
observable_type_type.domain_to_ipv6 = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'domain-to-ipv6', tag=u'domain_to_ipv6')
observable_type_type.domain_to_ipv4_timestamp = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'domain-to-ipv4-timestamp', tag=u'domain_to_ipv4_timestamp')
observable_type_type.domain_to_ipv6_timestamp = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'domain-to-ipv6-timestamp', tag=u'domain_to_ipv6_timestamp')
observable_type_type.ipv4_port = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv4-port', tag=u'ipv4_port')
observable_type_type.ipv6_port = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'ipv6-port', tag=u'ipv6_port')
observable_type_type.windows_reg_key = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'windows-reg-key', tag=u'windows_reg_key')
observable_type_type.file_hash = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'file-hash', tag=u'file_hash')
observable_type_type.email_x_mailer = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'email-x-mailer', tag=u'email_x_mailer')
observable_type_type.email_subject = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'email-subject', tag=u'email_subject')
observable_type_type.http_user_agent = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'http-user-agent', tag=u'http_user_agent')
observable_type_type.http_request_uri = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'http-request-uri', tag=u'http_request_uri')
observable_type_type.mutex = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'mutex', tag=u'mutex')
observable_type_type.file_path = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'file-path', tag=u'file_path')
observable_type_type.user_name = observable_type_type._CF_enumeration.addEnumeration(unicode_value=u'user-name', tag=u'user_name')
observable_type_type._InitializeFacetMap(observable_type_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'observable-type-type', observable_type_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}indicatorexpression-operator-type
class indicatorexpression_operator_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'indicatorexpression-operator-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1900, 3)
    _Documentation = None
indicatorexpression_operator_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=indicatorexpression_operator_type, enum_prefix=None)
indicatorexpression_operator_type.not_ = indicatorexpression_operator_type._CF_enumeration.addEnumeration(unicode_value=u'not', tag=u'not_')
indicatorexpression_operator_type.and_ = indicatorexpression_operator_type._CF_enumeration.addEnumeration(unicode_value=u'and', tag=u'and_')
indicatorexpression_operator_type.or_ = indicatorexpression_operator_type._CF_enumeration.addEnumeration(unicode_value=u'or', tag=u'or_')
indicatorexpression_operator_type.xor = indicatorexpression_operator_type._CF_enumeration.addEnumeration(unicode_value=u'xor', tag=u'xor')
indicatorexpression_operator_type._InitializeFacetMap(indicatorexpression_operator_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'indicatorexpression-operator-type', indicatorexpression_operator_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}PositiveFloatType
class PositiveFloatType (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PositiveFloatType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1938, 4)
    _Documentation = None
PositiveFloatType._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.float, value=pyxb.binding.datatypes.anySimpleType(u'0'))
PositiveFloatType._InitializeFacetMap(PositiveFloatType._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', u'PositiveFloatType', PositiveFloatType)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}PortlistType
class PortlistType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PortlistType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1954, 4)
    _Documentation = None
PortlistType._CF_pattern = pyxb.binding.facets.CF_pattern()
PortlistType._CF_pattern.addPattern(pattern=u'\\d+(\\-\\d+)?(,\\d+(\\-\\d+)?)*')
PortlistType._InitializeFacetMap(PortlistType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'PortlistType', PortlistType)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}yes-no-type
class yes_no_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'yes-no-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2000, 4)
    _Documentation = None
yes_no_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=yes_no_type, enum_prefix=None)
yes_no_type.yes = yes_no_type._CF_enumeration.addEnumeration(unicode_value=u'yes', tag=u'yes')
yes_no_type.no = yes_no_type._CF_enumeration.addEnumeration(unicode_value=u'no', tag=u'no')
yes_no_type._InitializeFacetMap(yes_no_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'yes-no-type', yes_no_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}yes-no-unknown-type
class yes_no_unknown_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'yes-no-unknown-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2007, 4)
    _Documentation = None
yes_no_unknown_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=yes_no_unknown_type, enum_prefix=None)
yes_no_unknown_type.yes = yes_no_unknown_type._CF_enumeration.addEnumeration(unicode_value=u'yes', tag=u'yes')
yes_no_unknown_type.no = yes_no_unknown_type._CF_enumeration.addEnumeration(unicode_value=u'no', tag=u'no')
yes_no_unknown_type.unknown = yes_no_unknown_type._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
yes_no_unknown_type._InitializeFacetMap(yes_no_unknown_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'yes-no-unknown-type', yes_no_unknown_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}restriction-type
class restriction_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'restriction-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2015, 4)
    _Documentation = None
restriction_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=restriction_type, enum_prefix=None)
restriction_type.default = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'default', tag=u'default')
restriction_type.public = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'public', tag=u'public')
restriction_type.partner = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'partner', tag=u'partner')
restriction_type.need_to_know = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'need-to-know', tag=u'need_to_know')
restriction_type.private = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'private', tag=u'private')
restriction_type.white = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'white', tag=u'white')
restriction_type.green = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'green', tag=u'green')
restriction_type.amber = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'amber', tag=u'amber')
restriction_type.red = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'red', tag=u'red')
restriction_type.ext_value = restriction_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
restriction_type._InitializeFacetMap(restriction_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'restriction-type', restriction_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}severity-type
class severity_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'severity-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2030, 4)
    _Documentation = None
severity_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=severity_type, enum_prefix=None)
severity_type.low = severity_type._CF_enumeration.addEnumeration(unicode_value=u'low', tag=u'low')
severity_type.medium = severity_type._CF_enumeration.addEnumeration(unicode_value=u'medium', tag=u'medium')
severity_type.high = severity_type._CF_enumeration.addEnumeration(unicode_value=u'high', tag=u'high')
severity_type._InitializeFacetMap(severity_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'severity-type', severity_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}duration-type
class duration_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'duration-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2038, 4)
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

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}action-type
class action_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'action-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2051, 4)
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
action_type.redirect_traffic = action_type._CF_enumeration.addEnumeration(unicode_value=u'redirect-traffic', tag=u'redirect_traffic')
action_type.honeypot = action_type._CF_enumeration.addEnumeration(unicode_value=u'honeypot', tag=u'honeypot')
action_type.upgrade_software = action_type._CF_enumeration.addEnumeration(unicode_value=u'upgrade-software', tag=u'upgrade_software')
action_type.rebuild_asset = action_type._CF_enumeration.addEnumeration(unicode_value=u'rebuild-asset', tag=u'rebuild_asset')
action_type.harden_asset = action_type._CF_enumeration.addEnumeration(unicode_value=u'harden-asset', tag=u'harden_asset')
action_type.remediate_other = action_type._CF_enumeration.addEnumeration(unicode_value=u'remediate-other', tag=u'remediate_other')
action_type.status_triage = action_type._CF_enumeration.addEnumeration(unicode_value=u'status-triage', tag=u'status_triage')
action_type.status_new_info = action_type._CF_enumeration.addEnumeration(unicode_value=u'status-new-info', tag=u'status_new_info')
action_type.watch_and_report = action_type._CF_enumeration.addEnumeration(unicode_value=u'watch-and-report', tag=u'watch_and_report')
action_type.defined_coa = action_type._CF_enumeration.addEnumeration(unicode_value=u'defined-coa', tag=u'defined_coa')
action_type.other = action_type._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
action_type.ext_value = action_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
action_type._InitializeFacetMap(action_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'action-type', action_type)

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}dtype-type
class dtype_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dtype-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2079, 4)
    _Documentation = None
dtype_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=dtype_type, enum_prefix=None)
dtype_type.boolean = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'boolean', tag=u'boolean')
dtype_type.byte = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
dtype_type.bytes = dtype_type._CF_enumeration.addEnumeration(unicode_value=u'bytes', tag=u'bytes')
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

# Atomic simple type: {urn:ietf:params:xml:ns:iodef-2.0}proto-dtype-type
class proto_dtype_type (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'proto-dtype-type')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 2105, 4)
    _Documentation = None
proto_dtype_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=proto_dtype_type, enum_prefix=None)
proto_dtype_type.boolean = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'boolean', tag=u'boolean')
proto_dtype_type.byte = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'byte', tag=u'byte')
proto_dtype_type.bytes = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'bytes', tag=u'bytes')
proto_dtype_type.character = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'character', tag=u'character')
proto_dtype_type.date_time = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'date-time', tag=u'date_time')
proto_dtype_type.integer = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'integer', tag=u'integer')
proto_dtype_type.real = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'real', tag=u'real')
proto_dtype_type.string = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
proto_dtype_type.xml = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'xml', tag=u'xml')
proto_dtype_type.ext_value = proto_dtype_type._CF_enumeration.addEnumeration(unicode_value=u'ext-value', tag=u'ext_value')
proto_dtype_type._InitializeFacetMap(proto_dtype_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'proto-dtype-type', proto_dtype_type)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 27, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Incident uses Python identifier Incident
    __Incident = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Incident'), 'Incident', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_urnietfparamsxmlnsiodef_2_0Incident', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 50, 4), )

    
    Incident = property(__Incident.value, __Incident.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 36, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_version', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'2.00')
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 34, 8)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 34, 8)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute format-id uses Python identifier format_id
    __format_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'format-id'), 'format_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_format_id', pyxb.binding.datatypes.string)
    __format_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 37, 8)
    __format_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 37, 8)
    
    format_id = property(__format_id.value, __format_id.set, None, None)

    
    # Attribute private-enum-name uses Python identifier private_enum_name
    __private_enum_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'private-enum-name'), 'private_enum_name', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_private_enum_name', pyxb.binding.datatypes.string)
    __private_enum_name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 39, 8)
    __private_enum_name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 39, 8)
    
    private_enum_name = property(__private_enum_name.value, __private_enum_name.set, None, None)

    
    # Attribute private-enum-id uses Python identifier private_enum_id
    __private_enum_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'private-enum-id'), 'private_enum_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_private_enum_id', pyxb.binding.datatypes.string)
    __private_enum_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 41, 8)
    __private_enum_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 41, 8)
    
    private_enum_id = property(__private_enum_id.value, __private_enum_id.set, None, None)

    _ElementMap.update({
        __Incident.name() : __Incident,
        __AdditionalData.name() : __AdditionalData
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __version.name() : __version,
        __format_id.name() : __format_id,
        __private_enum_name.name() : __private_enum_name,
        __private_enum_id.name() : __private_enum_id
    })



# Complex type {urn:ietf:params:xml:ns:iodef-2.0}ContactMeansType with content type SIMPLE
class ContactMeansType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-2.0}ContactMeansType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContactMeansType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 383, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_2_0_ContactMeansType_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 386, 10)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 386, 10)
    
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
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 597, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON__urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON__urnietfparamsxmlnsiodef_2_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-enum-1.0}ReferenceName uses Python identifier ReferenceName
    __ReferenceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_enum, u'ReferenceName'), 'ReferenceName', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON__urnietfparamsxmlnsiodef_enum_1_0ReferenceName', False, pyxb.utils.utility.Location(u'http://www.iana.org/assignments/xml-registry/schema/iodef-enum-1.0.xsd', 13, 1), )

    
    ReferenceName = property(__ReferenceName.value, __ReferenceName.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON__observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 606, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 606, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __Description.name() : __Description,
        __URL.name() : __URL,
        __ReferenceName.name() : __ReferenceName
    })
    _AttributeMap.update({
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 868, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}System uses Python identifier System
    __System = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'System'), 'System', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_2_urnietfparamsxmlnsiodef_2_0System', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 880, 4), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 948, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}PostalAddress uses Python identifier PostalAddress
    __PostalAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), 'PostalAddress', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_3_urnietfparamsxmlnsiodef_2_0PostalAddress', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 369, 4), )

    
    PostalAddress = property(__PostalAddress.value, __PostalAddress.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_3_urnietfparamsxmlnsiodef_2_0Address', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 967, 4), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Location'), 'Location', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_3_urnietfparamsxmlnsiodef_2_0Location', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1004, 4), )

    
    Location = property(__Location.value, __Location.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}NodeRole uses Python identifier NodeRole
    __NodeRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), 'NodeRole', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_3_urnietfparamsxmlnsiodef_2_0NodeRole', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1006, 4), )

    
    NodeRole = property(__NodeRole.value, __NodeRole.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_3_urnietfparamsxmlnsiodef_2_0Counter', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1136, 4), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DomainData uses Python identifier DomainData
    __DomainData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DomainData'), 'DomainData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_3_urnietfparamsxmlnsiodef_2_0DomainData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1218, 2), )

    
    DomainData = property(__DomainData.value, __DomainData.set, None, None)

    _ElementMap.update({
        __PostalAddress.name() : __PostalAddress,
        __Address.name() : __Address,
        __Location.name() : __Location,
        __NodeRole.name() : __NodeRole,
        __Counter.name() : __Counter,
        __DomainData.name() : __DomainData
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
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1085, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Port uses Python identifier Port
    __Port = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Port'), 'Port', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0Port', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1109, 4), )

    
    Port = property(__Port.value, __Port.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Portlist uses Python identifier Portlist
    __Portlist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Portlist'), 'Portlist', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0Portlist', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1110, 4), )

    
    Portlist = property(__Portlist.value, __Portlist.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ProtoType uses Python identifier ProtoType
    __ProtoType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoType'), 'ProtoType', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0ProtoType', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1111, 4), )

    
    ProtoType = property(__ProtoType.value, __ProtoType.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ProtoCode uses Python identifier ProtoCode
    __ProtoCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode'), 'ProtoCode', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0ProtoCode', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1112, 4), )

    
    ProtoCode = property(__ProtoCode.value, __ProtoCode.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ProtoField uses Python identifier ProtoField
    __ProtoField = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ProtoField'), 'ProtoField', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0ProtoField', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1113, 4), )

    
    ProtoField = property(__ProtoField.value, __ProtoField.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ApplicationHeader uses Python identifier ApplicationHeader
    __ApplicationHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeader'), 'ApplicationHeader', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0ApplicationHeader', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1114, 4), )

    
    ApplicationHeader = property(__ApplicationHeader.value, __ApplicationHeader.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ServiceName uses Python identifier ServiceName
    __ServiceName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ServiceName'), 'ServiceName', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0ServiceName', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1117, 4), )

    
    ServiceName = property(__ServiceName.value, __ServiceName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EmailData uses Python identifier EmailData
    __EmailData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EmailData'), 'EmailData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0EmailData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1190, 3), )

    
    EmailData = property(__EmailData.value, __EmailData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_urnietfparamsxmlnsiodef_2_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4), )

    
    Application = property(__Application.value, __Application.set, None, None)

    
    # Attribute ip-protocol uses Python identifier ip_protocol
    __ip_protocol = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ip-protocol'), 'ip_protocol', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_ip_protocol', pyxb.binding.datatypes.integer, required=True)
    __ip_protocol._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1102, 8)
    __ip_protocol._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1102, 8)
    
    ip_protocol = property(__ip_protocol.value, __ip_protocol.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_4_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1104, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1104, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __Port.name() : __Port,
        __Portlist.name() : __Portlist,
        __ProtoType.name() : __ProtoType,
        __ProtoCode.name() : __ProtoCode,
        __ProtoField.name() : __ProtoField,
        __ApplicationHeader.name() : __ApplicationHeader,
        __ServiceName.name() : __ServiceName,
        __EmailData.name() : __EmailData,
        __Application.name() : __Application
    })
    _AttributeMap.update({
        __ip_protocol.name() : __ip_protocol,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1118, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IANAService uses Python identifier IANAService
    __IANAService = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IANAService'), 'IANAService', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_5_urnietfparamsxmlnsiodef_2_0IANAService', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1129, 4), )

    
    IANAService = property(__IANAService.value, __IANAService.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_5_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_5_urnietfparamsxmlnsiodef_2_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    _ElementMap.update({
        __IANAService.name() : __IANAService,
        __Description.name() : __Description,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1191, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EmailFrom uses Python identifier EmailFrom
    __EmailFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EmailFrom'), 'EmailFrom', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_6_urnietfparamsxmlnsiodef_2_0EmailFrom', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1207, 3), )

    
    EmailFrom = property(__EmailFrom.value, __EmailFrom.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EmailSubject uses Python identifier EmailSubject
    __EmailSubject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EmailSubject'), 'EmailSubject', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_6_urnietfparamsxmlnsiodef_2_0EmailSubject', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1208, 3), )

    
    EmailSubject = property(__EmailSubject.value, __EmailSubject.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EmailX-Mailer uses Python identifier EmailX_Mailer
    __EmailX_Mailer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EmailX-Mailer'), 'EmailX_Mailer', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_6_urnietfparamsxmlnsiodef_2_0EmailX_Mailer', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1209, 3), )

    
    EmailX_Mailer = property(__EmailX_Mailer.value, __EmailX_Mailer.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EmailHeaderField uses Python identifier EmailHeaderField
    __EmailHeaderField = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EmailHeaderField'), 'EmailHeaderField', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_6_urnietfparamsxmlnsiodef_2_0EmailHeaderField', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1210, 3), )

    
    EmailHeaderField = property(__EmailHeaderField.value, __EmailHeaderField.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}HashData uses Python identifier HashData
    __HashData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HashData'), 'HashData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_6_urnietfparamsxmlnsiodef_2_0HashData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1543, 2), )

    
    HashData = property(__HashData.value, __HashData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}SignatureData uses Python identifier SignatureData
    __SignatureData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SignatureData'), 'SignatureData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_6_urnietfparamsxmlnsiodef_2_0SignatureData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1604, 2), )

    
    SignatureData = property(__SignatureData.value, __SignatureData.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_6_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1202, 7)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1202, 7)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __EmailFrom.name() : __EmailFrom,
        __EmailSubject.name() : __EmailSubject,
        __EmailX_Mailer.name() : __EmailX_Mailer,
        __EmailHeaderField.name() : __EmailHeaderField,
        __HashData.name() : __HashData,
        __SignatureData.name() : __SignatureData
    })
    _AttributeMap.update({
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1333, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_7_urnietfparamsxmlnsiodef_2_0Address', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 967, 4), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Server uses Python identifier Server
    __Server = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Server'), 'Server', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_7_urnietfparamsxmlnsiodef_2_0Server', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1341, 3), )

    
    Server = property(__Server.value, __Server.set, None, None)

    _ElementMap.update({
        __Address.name() : __Address,
        __Server.name() : __Server
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1344, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_8_urnietfparamsxmlnsiodef_2_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}SameDomainContact uses Python identifier SameDomainContact
    __SameDomainContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SameDomainContact'), 'SameDomainContact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_8_urnietfparamsxmlnsiodef_2_0SameDomainContact', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1353, 3), )

    
    SameDomainContact = property(__SameDomainContact.value, __SameDomainContact.set, None, None)

    _ElementMap.update({
        __Contact.name() : __Contact,
        __SameDomainContact.name() : __SameDomainContact
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1451, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Key uses Python identifier Key
    __Key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Key'), 'Key', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_9_urnietfparamsxmlnsiodef_2_0Key', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1461, 5), )

    
    Key = property(__Key.value, __Key.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_9_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1456, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1456, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __Key.name() : __Key
    })
    _AttributeMap.update({
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1511, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature'), 'Signature', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_urnietfparamsxmlnsiodef_2_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1522, 8), )

    
    Application = property(__Application.value, __Application.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}FileName uses Python identifier FileName
    __FileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileName'), 'FileName', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_urnietfparamsxmlnsiodef_2_0FileName', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1532, 3), )

    
    FileName = property(__FileName.value, __FileName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}FileSize uses Python identifier FileSize
    __FileSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileSize'), 'FileSize', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_urnietfparamsxmlnsiodef_2_0FileSize', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1533, 3), )

    
    FileSize = property(__FileSize.value, __FileSize.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}FileType uses Python identifier FileType
    __FileType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileType'), 'FileType', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_urnietfparamsxmlnsiodef_2_0FileType', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1534, 3), )

    
    FileType = property(__FileType.value, __FileType.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}FileProperties uses Python identifier FileProperties
    __FileProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileProperties'), 'FileProperties', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_urnietfparamsxmlnsiodef_2_0FileProperties', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1535, 3), )

    
    FileProperties = property(__FileProperties.value, __FileProperties.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}HashData uses Python identifier HashData
    __HashData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HashData'), 'HashData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_urnietfparamsxmlnsiodef_2_0HashData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1543, 2), )

    
    HashData = property(__HashData.value, __HashData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_urnietfparamsxmlnsiodef_2_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_10_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1527, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1527, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __Signature.name() : __Signature,
        __Application.name() : __Application,
        __FileName.name() : __FileName,
        __FileSize.name() : __FileSize,
        __FileType.name() : __FileType,
        __FileProperties.name() : __FileProperties,
        __HashData.name() : __HashData,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1577, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}CanonicalizationMethod uses Python identifier CanonicalizationMethod
    __CanonicalizationMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, u'CanonicalizationMethod'), 'CanonicalizationMethod', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_11_httpwww_w3_org200009xmldsigCanonicalizationMethod', False, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 75, 2), )

    
    CanonicalizationMethod = property(__CanonicalizationMethod.value, __CanonicalizationMethod.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestMethod uses Python identifier DigestMethod
    __DigestMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, u'DigestMethod'), 'DigestMethod', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_11_httpwww_w3_org200009xmldsigDigestMethod', False, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 127, 0), )

    
    DigestMethod = property(__DigestMethod.value, __DigestMethod.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}DigestValue uses Python identifier DigestValue
    __DigestValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, u'DigestValue'), 'DigestValue', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_11_httpwww_w3_org200009xmldsigDigestValue', False, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 135, 0), )

    
    DigestValue = property(__DigestValue.value, __DigestValue.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_11_urnietfparamsxmlnsiodef_2_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4), )

    
    Application = property(__Application.value, __Application.set, None, None)

    _ElementMap.update({
        __CanonicalizationMethod.name() : __CanonicalizationMethod,
        __DigestMethod.name() : __DigestMethod,
        __DigestValue.name() : __DigestValue,
        __Application.name() : __Application
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1589, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_12_urnietfparamsxmlnsiodef_2_0AdditionalData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_12_urnietfparamsxmlnsiodef_2_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4), )

    
    Application = property(__Application.value, __Application.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Application.name() : __Application
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1605, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature'), 'Signature', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_13_httpwww_w3_org200009xmldsigSignature', True, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    _ElementMap.update({
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1635, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2000/09/xmldsig#}X509Data uses Python identifier X509Data
    __X509Data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, u'X509Data'), 'X509Data', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_14_httpwww_w3_org200009xmldsigX509Data', False, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 183, 0), )

    
    X509Data = property(__X509Data.value, __X509Data.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_14_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1639, 5)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1639, 5)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __X509Data.name() : __X509Data
    })
    _AttributeMap.update({
        __observable_id.name() : __observable_id
    })



# Complex type {urn:ietf:params:xml:ns:iodef-2.0}SoftwareType with content type ELEMENT_ONLY
class SoftwareType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-2.0}SoftwareType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SoftwareType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1649, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}SoftwareReference uses Python identifier SoftwareReference
    __SoftwareReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SoftwareReference'), 'SoftwareReference', '__urnietfparamsxmlnsiodef_2_0_SoftwareType_urnietfparamsxmlnsiodef_2_0SoftwareReference', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1660, 4), )

    
    SoftwareReference = property(__SoftwareReference.value, __SoftwareReference.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_SoftwareType_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_2_0_SoftwareType_urnietfparamsxmlnsiodef_2_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    _ElementMap.update({
        __SoftwareReference.name() : __SoftwareReference,
        __Description.name() : __Description,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SoftwareType', SoftwareType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1708, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Indicator'), 'Indicator', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_15_urnietfparamsxmlnsiodef_2_0Indicator', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1716, 3), )

    
    Indicator = property(__Indicator.value, __Indicator.set, None, None)

    _ElementMap.update({
        __Indicator.name() : __Indicator
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.ID
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1747, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.ID
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_16_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1750, 11)
    __name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1750, 11)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_16_version', pyxb.binding.datatypes.string, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1752, 11)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1752, 11)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __version.name() : __version
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1867, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_17_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Hash uses Python identifier Hash
    __Hash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Hash'), 'Hash', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_17_urnietfparamsxmlnsiodef_2_0Hash', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1576, 2), )

    
    Hash = property(__Hash.value, __Hash.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Hash.name() : __Hash
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1910, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uid-ref uses Python identifier uid_ref
    __uid_ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid-ref'), 'uid_ref', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_18_uid_ref', pyxb.binding.datatypes.IDREF, required=True)
    __uid_ref._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1911, 7)
    __uid_ref._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1911, 7)
    
    uid_ref = property(__uid_ref.value, __uid_ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uid_ref.name() : __uid_ref
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1917, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uid-ref uses Python identifier uid_ref
    __uid_ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uid-ref'), 'uid_ref', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_19_uid_ref', pyxb.binding.datatypes.IDREF)
    __uid_ref._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1918, 7)
    __uid_ref._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1918, 7)
    
    uid_ref = property(__uid_ref.value, __uid_ref.set, None, None)

    
    # Attribute euid-ref uses Python identifier euid_ref
    __euid_ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'euid-ref'), 'euid_ref', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_19_euid_ref', pyxb.binding.datatypes.string)
    __euid_ref._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1920, 7)
    __euid_ref._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1920, 7)
    
    euid_ref = property(__euid_ref.value, __euid_ref.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_19_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1922, 7)
    __version._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1922, 7)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uid_ref.name() : __uid_ref,
        __euid_ref.name() : __euid_ref,
        __version.name() : __version
    })



# Complex type {urn:ietf:params:xml:ns:iodef-2.0}MLStringType with content type SIMPLE
class MLStringType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-2.0}MLStringType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MLStringType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1944, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__urnietfparamsxmlnsiodef_2_0_MLStringType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1949, 10)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute translation-id uses Python identifier translation_id
    __translation_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'translation-id'), 'translation_id', '__urnietfparamsxmlnsiodef_2_0_MLStringType_translation_id', pyxb.binding.datatypes.string)
    __translation_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1947, 10)
    __translation_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1947, 10)
    
    translation_id = property(__translation_id.value, __translation_id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __translation_id.name() : __translation_id
    })
Namespace.addCategoryObject('typeBinding', u'MLStringType', MLStringType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 51, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0IncidentID', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AlternativeID uses Python identifier AlternativeID
    __AlternativeID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), 'AlternativeID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0AlternativeID', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 153, 4), )

    
    AlternativeID = property(__AlternativeID.value, __AlternativeID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RelatedActivity uses Python identifier RelatedActivity
    __RelatedActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), 'RelatedActivity', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0RelatedActivity', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 170, 4), )

    
    RelatedActivity = property(__RelatedActivity.value, __RelatedActivity.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ReportTime uses Python identifier ReportTime
    __ReportTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), 'ReportTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0ReportTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 399, 4), )

    
    ReportTime = property(__ReportTime.value, __ReportTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DetectTime uses Python identifier DetectTime
    __DetectTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), 'DetectTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0DetectTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 401, 4), )

    
    DetectTime = property(__DetectTime.value, __DetectTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RecoveryTime uses Python identifier RecoveryTime
    __RecoveryTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecoveryTime'), 'RecoveryTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0RecoveryTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 407, 4), )

    
    RecoveryTime = property(__RecoveryTime.value, __RecoveryTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}GenerationTime uses Python identifier GenerationTime
    __GenerationTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'GenerationTime'), 'GenerationTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0GenerationTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 409, 4), )

    
    GenerationTime = property(__GenerationTime.value, __GenerationTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}History uses Python identifier History
    __History = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'History'), 'History', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0History', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 423, 4), )

    
    History = property(__History.value, __History.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Discovery uses Python identifier Discovery
    __Discovery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Discovery'), 'Discovery', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0Discovery', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 505, 4), )

    
    Discovery = property(__Discovery.value, __Discovery.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Method uses Python identifier Method
    __Method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Method'), 'Method', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0Method', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 574, 4), )

    
    Method = property(__Method.value, __Method.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Assessment uses Python identifier Assessment
    __Assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), 'Assessment', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0Assessment', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 616, 4), )

    
    Assessment = property(__Assessment.value, __Assessment.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EventData uses Python identifier EventData
    __EventData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventData'), 'EventData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0EventData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 819, 4), )

    
    EventData = property(__EventData.value, __EventData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 93, 8)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute purpose uses Python identifier purpose
    __purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'purpose'), 'purpose', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_purpose', incident_purpose_type, required=True)
    __purpose._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 86, 8)
    __purpose._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 86, 8)
    
    purpose = property(__purpose.value, __purpose.set, None, None)

    
    # Attribute ext-purpose uses Python identifier ext_purpose
    __ext_purpose = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-purpose'), 'ext_purpose', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_ext_purpose', pyxb.binding.datatypes.string)
    __ext_purpose._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 88, 8)
    __ext_purpose._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 88, 8)
    
    ext_purpose = property(__ext_purpose.value, __ext_purpose.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_status', incident_status_type)
    __status._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 90, 8)
    __status._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 90, 8)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute ext-status uses Python identifier ext_status
    __ext_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-status'), 'ext_status', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_ext_status', pyxb.binding.datatypes.string)
    __ext_status._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 91, 8)
    __ext_status._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 91, 8)
    
    ext_status = property(__ext_status.value, __ext_status.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_restriction', restriction_type, unicode_default=u'private')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 94, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 94, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 97, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 97, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_20_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 99, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 99, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

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
        __RecoveryTime.name() : __RecoveryTime,
        __GenerationTime.name() : __GenerationTime,
        __History.name() : __History,
        __Discovery.name() : __Discovery,
        __Method.name() : __Method,
        __Assessment.name() : __Assessment,
        __EventData.name() : __EventData,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __purpose.name() : __purpose,
        __ext_purpose.name() : __ext_purpose,
        __status.name() : __status,
        __ext_status.name() : __ext_status,
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction,
        __observable_id.name() : __observable_id
    })



# Complex type {urn:ietf:params:xml:ns:iodef-2.0}IncidentIDType with content type SIMPLE
class IncidentIDType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-2.0}IncidentIDType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IncidentIDType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 132, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__urnietfparamsxmlnsiodef_2_0_IncidentIDType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 135, 10)
    __name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 135, 10)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute instance uses Python identifier instance
    __instance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instance'), 'instance', '__urnietfparamsxmlnsiodef_2_0_IncidentIDType_instance', pyxb.binding.datatypes.string)
    __instance._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 137, 10)
    __instance._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 137, 10)
    
    instance = property(__instance.value, __instance.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_IncidentIDType_restriction', restriction_type, unicode_default=u'public')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 139, 10)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 139, 10)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_IncidentIDType_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 142, 10)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 142, 10)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __instance.name() : __instance,
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })
Namespace.addCategoryObject('typeBinding', u'IncidentIDType', IncidentIDType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 154, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_21_urnietfparamsxmlnsiodef_2_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_21_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 159, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 159, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_21_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 161, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 161, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 171, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_urnietfparamsxmlnsiodef_2_0IncidentID', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ThreatActor uses Python identifier ThreatActor
    __ThreatActor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ThreatActor'), 'ThreatActor', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_urnietfparamsxmlnsiodef_2_0ThreatActor', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 202, 4), )

    
    ThreatActor = property(__ThreatActor.value, __ThreatActor.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Campaign uses Python identifier Campaign
    __Campaign = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Campaign'), 'Campaign', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_urnietfparamsxmlnsiodef_2_0Campaign', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 231, 4), )

    
    Campaign = property(__Campaign.value, __Campaign.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Confidence uses Python identifier Confidence
    __Confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), 'Confidence', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_urnietfparamsxmlnsiodef_2_0Confidence', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 797, 4), )

    
    Confidence = property(__Confidence.value, __Confidence.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_urnietfparamsxmlnsiodef_2_0URL', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 190, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 190, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_22_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 192, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 192, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID,
        __ThreatActor.name() : __ThreatActor,
        __Campaign.name() : __Campaign,
        __AdditionalData.name() : __AdditionalData,
        __Confidence.name() : __Confidence,
        __Description.name() : __Description,
        __URL.name() : __URL
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 203, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ThreatActorID uses Python identifier ThreatActorID
    __ThreatActorID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ThreatActorID'), 'ThreatActorID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_23_urnietfparamsxmlnsiodef_2_0ThreatActorID', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 224, 4), )

    
    ThreatActorID = property(__ThreatActorID.value, __ThreatActorID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_23_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_23_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_23_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 217, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 217, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_23_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 219, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 219, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __ThreatActorID.name() : __ThreatActorID,
        __AdditionalData.name() : __AdditionalData,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 232, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}CampaignID uses Python identifier CampaignID
    __CampaignID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CampaignID'), 'CampaignID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_24_urnietfparamsxmlnsiodef_2_0CampaignID', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 252, 4), )

    
    CampaignID = property(__CampaignID.value, __CampaignID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_24_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_24_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_24_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 246, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 246, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_24_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 248, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 248, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __CampaignID.name() : __CampaignID,
        __AdditionalData.name() : __AdditionalData,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 267, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ContactName uses Python identifier ContactName
    __ContactName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), 'ContactName', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0ContactName', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 339, 4), )

    
    ContactName = property(__ContactName.value, __ContactName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ContactTitle uses Python identifier ContactTitle
    __ContactTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ContactTitle'), 'ContactTitle', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0ContactTitle', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 341, 4), )

    
    ContactTitle = property(__ContactTitle.value, __ContactTitle.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RegistryHandle uses Python identifier RegistryHandle
    __RegistryHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), 'RegistryHandle', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0RegistryHandle', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 343, 4), )

    
    RegistryHandle = property(__RegistryHandle.value, __RegistryHandle.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}PostalAddress uses Python identifier PostalAddress
    __PostalAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), 'PostalAddress', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0PostalAddress', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 369, 4), )

    
    PostalAddress = property(__PostalAddress.value, __PostalAddress.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Email uses Python identifier Email
    __Email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Email'), 'Email', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0Email', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 379, 4), )

    
    Email = property(__Email.value, __Email.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Telephone uses Python identifier Telephone
    __Telephone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), 'Telephone', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0Telephone', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 380, 4), )

    
    Telephone = property(__Telephone.value, __Telephone.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Fax uses Python identifier Fax
    __Fax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Fax'), 'Fax', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0Fax', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 381, 4), )

    
    Fax = property(__Fax.value, __Fax.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Timezone uses Python identifier Timezone
    __Timezone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), 'Timezone', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0Timezone', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 411, 4), )

    
    Timezone = property(__Timezone.value, __Timezone.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_role', contact_role_type, required=True)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 292, 8)
    __role._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 292, 8)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute ext-role uses Python identifier ext_role
    __ext_role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-role'), 'ext_role', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_ext_role', pyxb.binding.datatypes.string)
    __ext_role._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 294, 8)
    __ext_role._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 294, 8)
    
    ext_role = property(__ext_role.value, __ext_role.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_type', contact_type_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 296, 8)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 296, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 298, 8)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 298, 8)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 300, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 300, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_25_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 302, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 302, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Contact.name() : __Contact,
        __ContactName.name() : __ContactName,
        __ContactTitle.name() : __ContactTitle,
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
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 344, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute registry uses Python identifier registry
    __registry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'registry'), 'registry', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_26_registry', registryhandle_registry_type)
    __registry._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 347, 12)
    __registry._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 347, 12)
    
    registry = property(__registry.value, __registry.set, None, None)

    
    # Attribute ext-registry uses Python identifier ext_registry
    __ext_registry = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-registry'), 'ext_registry', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_26_ext_registry', pyxb.binding.datatypes.string)
    __ext_registry._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 349, 12)
    __ext_registry._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 349, 12)
    
    ext_registry = property(__ext_registry.value, __ext_registry.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __registry.name() : __registry,
        __ext_registry.name() : __ext_registry
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_27 (MLStringType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 370, 6)
    _ElementMap = MLStringType._ElementMap.copy()
    _AttributeMap = MLStringType._AttributeMap.copy()
    # Base type is MLStringType
    
    # Attribute lang inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_27_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 373, 12)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 373, 12)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute translation_id inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __meaning.name() : __meaning
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 424, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}HistoryItem uses Python identifier HistoryItem
    __HistoryItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), 'HistoryItem', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_28_urnietfparamsxmlnsiodef_2_0HistoryItem', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 436, 4), )

    
    HistoryItem = property(__HistoryItem.value, __HistoryItem.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_28_restriction', restriction_type, unicode_default=u'default')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 429, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 429, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_28_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 432, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 432, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __HistoryItem.name() : __HistoryItem
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 437, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IncidentID uses Python identifier IncidentID
    __IncidentID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), 'IncidentID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_urnietfparamsxmlnsiodef_2_0IncidentID', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4), )

    
    IncidentID = property(__IncidentID.value, __IncidentID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_urnietfparamsxmlnsiodef_2_0Contact', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_urnietfparamsxmlnsiodef_2_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 397, 4), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DefinedCOA uses Python identifier DefinedCOA
    __DefinedCOA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DefinedCOA'), 'DefinedCOA', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_urnietfparamsxmlnsiodef_2_0DefinedCOA', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 463, 4), )

    
    DefinedCOA = property(__DefinedCOA.value, __DefinedCOA.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 451, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 451, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 453, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 453, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_action', action_type, required=True)
    __action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 455, 8)
    __action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 455, 8)
    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute ext-action uses Python identifier ext_action
    __ext_action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-action'), 'ext_action', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_ext_action', pyxb.binding.datatypes.string)
    __ext_action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 457, 8)
    __ext_action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 457, 8)
    
    ext_action = property(__ext_action.value, __ext_action.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_29_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 459, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 459, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __IncidentID.name() : __IncidentID,
        __AdditionalData.name() : __AdditionalData,
        __Contact.name() : __Contact,
        __DateTime.name() : __DateTime,
        __DefinedCOA.name() : __DefinedCOA,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction,
        __action.name() : __action,
        __ext_action.name() : __ext_action,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 471, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_urnietfparamsxmlnsiodef_2_0Contact', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_urnietfparamsxmlnsiodef_2_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_urnietfparamsxmlnsiodef_2_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DefinedCOA uses Python identifier DefinedCOA
    __DefinedCOA = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DefinedCOA'), 'DefinedCOA', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_urnietfparamsxmlnsiodef_2_0DefinedCOA', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 463, 4), )

    
    DefinedCOA = property(__DefinedCOA.value, __DefinedCOA.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_restriction', restriction_type, unicode_default=u'default')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 484, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 484, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 487, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 487, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 489, 8)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 489, 8)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'action'), 'action', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_action', action_type, unicode_default=u'other')
    __action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 491, 8)
    __action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 491, 8)
    
    action = property(__action.value, __action.set, None, None)

    
    # Attribute ext-action uses Python identifier ext_action
    __ext_action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-action'), 'ext_action', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_ext_action', pyxb.binding.datatypes.string)
    __ext_action._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 493, 8)
    __ext_action._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 493, 8)
    
    ext_action = property(__ext_action.value, __ext_action.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_30_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 495, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 495, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __Contact.name() : __Contact,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __DefinedCOA.name() : __DefinedCOA,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction,
        __severity.name() : __severity,
        __action.name() : __action,
        __ext_action.name() : __ext_action,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 506, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_31_urnietfparamsxmlnsiodef_2_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DetectionPattern uses Python identifier DetectionPattern
    __DetectionPattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectionPattern'), 'DetectionPattern', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_31_urnietfparamsxmlnsiodef_2_0DetectionPattern', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 552, 4), )

    
    DetectionPattern = property(__DetectionPattern.value, __DetectionPattern.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_31_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'source'), 'source', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_31_source', discovery_source_type, unicode_default=u'unknown')
    __source._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 515, 8)
    __source._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 515, 8)
    
    source = property(__source.value, __source.set, None, None)

    
    # Attribute ext-source uses Python identifier ext_source
    __ext_source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-source'), 'ext_source', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_31_ext_source', pyxb.binding.datatypes.string)
    __ext_source._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 518, 8)
    __ext_source._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 518, 8)
    
    ext_source = property(__ext_source.value, __ext_source.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_31_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 520, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 520, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_31_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 522, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 522, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __Contact.name() : __Contact,
        __DetectionPattern.name() : __DetectionPattern,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __source.name() : __source,
        __ext_source.name() : __ext_source,
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 553, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DetectionConfiguration uses Python identifier DetectionConfiguration
    __DetectionConfiguration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectionConfiguration'), 'DetectionConfiguration', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_32_urnietfparamsxmlnsiodef_2_0DetectionConfiguration', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 558, 10), )

    
    DetectionConfiguration = property(__DetectionConfiguration.value, __DetectionConfiguration.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_32_urnietfparamsxmlnsiodef_2_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4), )

    
    Application = property(__Application.value, __Application.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_32_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_32_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 562, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 562, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_32_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 564, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 564, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __DetectionConfiguration.name() : __DetectionConfiguration,
        __Application.name() : __Application,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 575, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_33_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_33_urnietfparamsxmlnsiodef_2_0Reference', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 596, 4), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_33_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_33_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 584, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 584, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_33_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 586, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 586, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Reference.name() : __Reference,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 617, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IncidentCategory uses Python identifier IncidentCategory
    __IncidentCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IncidentCategory'), 'IncidentCategory', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0IncidentCategory', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 653, 4), )

    
    IncidentCategory = property(__IncidentCategory.value, __IncidentCategory.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}BusinessImpact uses Python identifier BusinessImpact
    __BusinessImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'BusinessImpact'), 'BusinessImpact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0BusinessImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 654, 4), )

    
    BusinessImpact = property(__BusinessImpact.value, __BusinessImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IntendedImpact uses Python identifier IntendedImpact
    __IntendedImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IntendedImpact'), 'IntendedImpact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0IntendedImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 656, 4), )

    
    IntendedImpact = property(__IntendedImpact.value, __IntendedImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}MitigatingFactor uses Python identifier MitigatingFactor
    __MitigatingFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'MitigatingFactor'), 'MitigatingFactor', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0MitigatingFactor', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 658, 4), )

    
    MitigatingFactor = property(__MitigatingFactor.value, __MitigatingFactor.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}SystemImpact uses Python identifier SystemImpact
    __SystemImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SystemImpact'), 'SystemImpact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0SystemImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 661, 4), )

    
    SystemImpact = property(__SystemImpact.value, __SystemImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}TimeImpact uses Python identifier TimeImpact
    __TimeImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), 'TimeImpact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0TimeImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 760, 4), )

    
    TimeImpact = property(__TimeImpact.value, __TimeImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}MonetaryImpact uses Python identifier MonetaryImpact
    __MonetaryImpact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), 'MonetaryImpact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0MonetaryImpact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 784, 4), )

    
    MonetaryImpact = property(__MonetaryImpact.value, __MonetaryImpact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Confidence uses Python identifier Confidence
    __Confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), 'Confidence', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0Confidence', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 797, 4), )

    
    Confidence = property(__Confidence.value, __Confidence.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_urnietfparamsxmlnsiodef_2_0Counter', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1136, 4), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    
    # Attribute occurrence uses Python identifier occurrence
    __occurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'occurrence'), 'occurrence', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_occurrence', STD_ANON)
    __occurrence._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 636, 8)
    __occurrence._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 636, 8)
    
    occurrence = property(__occurrence.value, __occurrence.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 644, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 644, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 646, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 646, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_34_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 648, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 648, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __IncidentCategory.name() : __IncidentCategory,
        __BusinessImpact.name() : __BusinessImpact,
        __IntendedImpact.name() : __IntendedImpact,
        __MitigatingFactor.name() : __MitigatingFactor,
        __SystemImpact.name() : __SystemImpact,
        __TimeImpact.name() : __TimeImpact,
        __MonetaryImpact.name() : __MonetaryImpact,
        __Confidence.name() : __Confidence,
        __Counter.name() : __Counter
    })
    _AttributeMap.update({
        __occurrence.name() : __occurrence,
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_35 (MLStringType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 662, 6)
    _ElementMap = MLStringType._ElementMap.copy()
    _AttributeMap = MLStringType._AttributeMap.copy()
    # Base type is MLStringType
    
    # Attribute lang inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_35_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 665, 12)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 665, 12)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute completion uses Python identifier completion
    __completion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'completion'), 'completion', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_35_completion', STD_ANON_)
    __completion._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 667, 12)
    __completion._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 667, 12)
    
    completion = property(__completion.value, __completion.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_35_type', systemimpact_type_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 675, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 675, 12)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_35_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 678, 12)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 678, 12)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute translation_id inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __completion.name() : __completion,
        __type.name() : __type,
        __ext_type.name() : __ext_type
    })



# Complex type {urn:ietf:params:xml:ns:iodef-2.0}BusinessImpactType with content type SIMPLE
class BusinessImpactType (MLStringType):
    """Complex type {urn:ietf:params:xml:ns:iodef-2.0}BusinessImpactType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BusinessImpactType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 714, 4)
    _ElementMap = MLStringType._ElementMap.copy()
    _AttributeMap = MLStringType._AttributeMap.copy()
    # Base type is MLStringType
    
    # Attribute lang inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_2_0_BusinessImpactType_severity', businessimpact_severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 717, 10)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 717, 10)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute ext-severity uses Python identifier ext_severity
    __ext_severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-severity'), 'ext_severity', '__urnietfparamsxmlnsiodef_2_0_BusinessImpactType_ext_severity', pyxb.binding.datatypes.string)
    __ext_severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 720, 10)
    __ext_severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 720, 10)
    
    ext_severity = property(__ext_severity.value, __ext_severity.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_2_0_BusinessImpactType_type', businessimpact_type_type)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 722, 10)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 722, 10)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_2_0_BusinessImpactType_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 725, 10)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 725, 10)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute translation_id inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __ext_severity.name() : __ext_severity,
        __type.name() : __type,
        __ext_type.name() : __ext_type
    })
Namespace.addCategoryObject('typeBinding', u'BusinessImpactType', BusinessImpactType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = PositiveFloatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 761, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is PositiveFloatType
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_36_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 764, 12)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 764, 12)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute metric uses Python identifier metric
    __metric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'metric'), 'metric', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_36_metric', timeimpact_metric_type, required=True)
    __metric._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 766, 12)
    __metric._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 766, 12)
    
    metric = property(__metric.value, __metric.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_36_duration', duration_type)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 768, 12)
    __duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 768, 12)
    
    duration = property(__duration.value, __duration.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __metric.name() : __metric,
        __duration.name() : __duration
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = PositiveFloatType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 785, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is PositiveFloatType
    
    # Attribute severity uses Python identifier severity
    __severity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'severity'), 'severity', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_37_severity', severity_type)
    __severity._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 788, 12)
    __severity._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 788, 12)
    
    severity = property(__severity.value, __severity.set, None, None)

    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'currency'), 'currency', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_37_currency', pyxb.binding.datatypes.string)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 790, 12)
    __currency._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 790, 12)
    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __severity.name() : __severity,
        __currency.name() : __currency
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 798, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rating uses Python identifier rating
    __rating = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rating'), 'rating', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_38_rating', confidence_rating_type, required=True)
    __rating._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 799, 8)
    __rating._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 799, 8)
    
    rating = property(__rating.value, __rating.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rating.name() : __rating
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 820, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ReportTime uses Python identifier ReportTime
    __ReportTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), 'ReportTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0ReportTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 399, 4), )

    
    ReportTime = property(__ReportTime.value, __ReportTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DetectTime uses Python identifier DetectTime
    __DetectTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), 'DetectTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0DetectTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 401, 4), )

    
    DetectTime = property(__DetectTime.value, __DetectTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RecoveryTime uses Python identifier RecoveryTime
    __RecoveryTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecoveryTime'), 'RecoveryTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0RecoveryTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 407, 4), )

    
    RecoveryTime = property(__RecoveryTime.value, __RecoveryTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Expectation uses Python identifier Expectation
    __Expectation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), 'Expectation', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Expectation', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 470, 4), )

    
    Expectation = property(__Expectation.value, __Expectation.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Discovery uses Python identifier Discovery
    __Discovery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Discovery'), 'Discovery', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Discovery', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 505, 4), )

    
    Discovery = property(__Discovery.value, __Discovery.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Method uses Python identifier Method
    __Method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Method'), 'Method', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Method', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 574, 4), )

    
    Method = property(__Method.value, __Method.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Assessment uses Python identifier Assessment
    __Assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), 'Assessment', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Assessment', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 616, 4), )

    
    Assessment = property(__Assessment.value, __Assessment.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EventData uses Python identifier EventData
    __EventData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventData'), 'EventData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0EventData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 819, 4), )

    
    EventData = property(__EventData.value, __EventData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Flow uses Python identifier Flow
    __Flow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Flow'), 'Flow', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Flow', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 867, 4), )

    
    Flow = property(__Flow.value, __Flow.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Record uses Python identifier Record
    __Record = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Record'), 'Record', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Record', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1360, 4), )

    
    Record = property(__Record.value, __Record.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_restriction', restriction_type, unicode_default=u'default')
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 853, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 853, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 856, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 856, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_39_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 858, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 858, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __Contact.name() : __Contact,
        __ReportTime.name() : __ReportTime,
        __DetectTime.name() : __DetectTime,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __RecoveryTime.name() : __RecoveryTime,
        __Expectation.name() : __Expectation,
        __Discovery.name() : __Discovery,
        __Method.name() : __Method,
        __Assessment.name() : __Assessment,
        __EventData.name() : __EventData,
        __Flow.name() : __Flow,
        __Record.name() : __Record,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 881, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AssetID uses Python identifier AssetID
    __AssetID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AssetID'), 'AssetID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0AssetID', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 892, 10), )

    
    AssetID = property(__AssetID.value, __AssetID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Node uses Python identifier Node
    __Node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Node'), 'Node', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0Node', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 947, 4), )

    
    Node = property(__Node.value, __Node.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}NodeRole uses Python identifier NodeRole
    __NodeRole = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), 'NodeRole', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0NodeRole', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1006, 4), )

    
    NodeRole = property(__NodeRole.value, __NodeRole.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Service'), 'Service', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0Service', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1084, 4), )

    
    Service = property(__Service.value, __Service.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Counter uses Python identifier Counter
    __Counter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Counter'), 'Counter', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0Counter', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1136, 4), )

    
    Counter = property(__Counter.value, __Counter.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}OperatingSystem uses Python identifier OperatingSystem
    __OperatingSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), 'OperatingSystem', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0OperatingSystem', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1700, 4), )

    
    OperatingSystem = property(__OperatingSystem.value, __OperatingSystem.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 899, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 899, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 901, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 901, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_category', system_category_type)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 903, 8)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 903, 8)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext-category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-category'), 'ext_category', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 904, 8)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 904, 8)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute interface uses Python identifier interface
    __interface = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'interface'), 'interface', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_interface', pyxb.binding.datatypes.string)
    __interface._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 906, 8)
    __interface._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 906, 8)
    
    interface = property(__interface.value, __interface.set, None, None)

    
    # Attribute spoofed uses Python identifier spoofed
    __spoofed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'spoofed'), 'spoofed', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_spoofed', yes_no_unknown_type, unicode_default=u'unknown')
    __spoofed._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 908, 8)
    __spoofed._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 908, 8)
    
    spoofed = property(__spoofed.value, __spoofed.set, None, None)

    
    # Attribute virtual uses Python identifier virtual
    __virtual = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'virtual'), 'virtual', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_virtual', yes_no_unknown_type, unicode_default=u'unknown')
    __virtual._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 910, 8)
    __virtual._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 910, 8)
    
    virtual = property(__virtual.value, __virtual.set, None, None)

    
    # Attribute ownership uses Python identifier ownership
    __ownership = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ownership'), 'ownership', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_ownership', system_ownership_type)
    __ownership._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 912, 8)
    __ownership._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 912, 8)
    
    ownership = property(__ownership.value, __ownership.set, None, None)

    
    # Attribute ext-ownership uses Python identifier ext_ownership
    __ext_ownership = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-ownership'), 'ext_ownership', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_40_ext_ownership', pyxb.binding.datatypes.string)
    __ext_ownership._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 914, 8)
    __ext_ownership._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 914, 8)
    
    ext_ownership = property(__ext_ownership.value, __ext_ownership.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __AssetID.name() : __AssetID,
        __Node.name() : __Node,
        __NodeRole.name() : __NodeRole,
        __Service.name() : __Service,
        __Counter.name() : __Counter,
        __OperatingSystem.name() : __OperatingSystem,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction,
        __category.name() : __category,
        __ext_category.name() : __ext_category,
        __interface.name() : __interface,
        __spoofed.name() : __spoofed,
        __virtual.name() : __virtual,
        __ownership.name() : __ownership,
        __ext_ownership.name() : __ext_ownership
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 968, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_41_category', address_category_type, unicode_default=u'ipv4-addr')
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 971, 12)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 971, 12)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext-category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-category'), 'ext_category', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_41_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 974, 12)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 974, 12)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute vlan-name uses Python identifier vlan_name
    __vlan_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vlan-name'), 'vlan_name', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_41_vlan_name', pyxb.binding.datatypes.string)
    __vlan_name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 976, 12)
    __vlan_name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 976, 12)
    
    vlan_name = property(__vlan_name.value, __vlan_name.set, None, None)

    
    # Attribute vlan-num uses Python identifier vlan_num
    __vlan_num = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vlan-num'), 'vlan_num', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_41_vlan_num', pyxb.binding.datatypes.integer)
    __vlan_num._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 978, 12)
    __vlan_num._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 978, 12)
    
    vlan_num = property(__vlan_num.value, __vlan_num.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_41_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 980, 12)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 980, 12)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __category.name() : __category,
        __ext_category.name() : __ext_category,
        __vlan_name.name() : __vlan_name,
        __vlan_num.name() : __vlan_num,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_42 (MLStringType):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1007, 6)
    _ElementMap = MLStringType._ElementMap.copy()
    _AttributeMap = MLStringType._AttributeMap.copy()
    # Base type is MLStringType
    
    # Attribute lang inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_42_category', noderole_category_type, required=True)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1010, 12)
    __category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1010, 12)
    
    category = property(__category.value, __category.set, None, None)

    
    # Attribute ext-category uses Python identifier ext_category
    __ext_category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-category'), 'ext_category', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_42_ext_category', pyxb.binding.datatypes.string)
    __ext_category._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1013, 12)
    __ext_category._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1013, 12)
    
    ext_category = property(__ext_category.value, __ext_category.set, None, None)

    
    # Attribute translation_id inherited from {urn:ietf:params:xml:ns:iodef-2.0}MLStringType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __category.name() : __category,
        __ext_category.name() : __ext_category
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.double
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1137, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.double
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_43_type', counter_type_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1140, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1140, 12)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute unit uses Python identifier unit
    __unit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unit'), 'unit', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_43_unit', counter_unit_type, required=True)
    __unit._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1143, 12)
    __unit._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1143, 12)
    
    unit = property(__unit.value, __unit.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_43_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1146, 12)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1146, 12)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_43_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1148, 12)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1148, 12)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_43_duration', duration_type)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1150, 12)
    __duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1150, 12)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute ext-duration uses Python identifier ext_duration
    __ext_duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-duration'), 'ext_duration', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_43_ext_duration', pyxb.binding.datatypes.string)
    __ext_duration._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1152, 12)
    __ext_duration._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1152, 12)
    
    ext_duration = property(__ext_duration.value, __ext_duration.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __unit.name() : __unit,
        __ext_type.name() : __ext_type,
        __meaning.name() : __meaning,
        __duration.name() : __duration,
        __ext_duration.name() : __ext_duration
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1219, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_urnietfparamsxmlnsiodef_2_0Name', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1248, 2), )

    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DateDomainWasChecked uses Python identifier DateDomainWasChecked
    __DateDomainWasChecked = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateDomainWasChecked'), 'DateDomainWasChecked', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_urnietfparamsxmlnsiodef_2_0DateDomainWasChecked', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1249, 2), )

    
    DateDomainWasChecked = property(__DateDomainWasChecked.value, __DateDomainWasChecked.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RegistrationDate uses Python identifier RegistrationDate
    __RegistrationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RegistrationDate'), 'RegistrationDate', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_urnietfparamsxmlnsiodef_2_0RegistrationDate', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1250, 2), )

    
    RegistrationDate = property(__RegistrationDate.value, __RegistrationDate.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ExpirationDate uses Python identifier ExpirationDate
    __ExpirationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ExpirationDate'), 'ExpirationDate', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_urnietfparamsxmlnsiodef_2_0ExpirationDate', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1251, 2), )

    
    ExpirationDate = property(__ExpirationDate.value, __ExpirationDate.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RelatedDNS uses Python identifier RelatedDNS
    __RelatedDNS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RelatedDNS'), 'RelatedDNS', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_urnietfparamsxmlnsiodef_2_0RelatedDNS', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1280, 2), )

    
    RelatedDNS = property(__RelatedDNS.value, __RelatedDNS.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Nameservers uses Python identifier Nameservers
    __Nameservers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Nameservers'), 'Nameservers', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_urnietfparamsxmlnsiodef_2_0Nameservers', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1332, 3), )

    
    Nameservers = property(__Nameservers.value, __Nameservers.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DomainContacts uses Python identifier DomainContacts
    __DomainContacts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DomainContacts'), 'DomainContacts', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_urnietfparamsxmlnsiodef_2_0DomainContacts', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1343, 3), )

    
    DomainContacts = property(__DomainContacts.value, __DomainContacts.set, None, None)

    
    # Attribute system-status uses Python identifier system_status
    __system_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'system-status'), 'system_status', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_system_status', domaindata_system_status_type)
    __system_status._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1235, 6)
    __system_status._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1235, 6)
    
    system_status = property(__system_status.value, __system_status.set, None, None)

    
    # Attribute ext-system-status uses Python identifier ext_system_status
    __ext_system_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-system-status'), 'ext_system_status', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_ext_system_status', pyxb.binding.datatypes.string)
    __ext_system_status._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1237, 6)
    __ext_system_status._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1237, 6)
    
    ext_system_status = property(__ext_system_status.value, __ext_system_status.set, None, None)

    
    # Attribute domain-status uses Python identifier domain_status
    __domain_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'domain-status'), 'domain_status', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_domain_status', domaindata_domain_status_type)
    __domain_status._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1239, 6)
    __domain_status._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1239, 6)
    
    domain_status = property(__domain_status.value, __domain_status.set, None, None)

    
    # Attribute ext-domain-status uses Python identifier ext_domain_status
    __ext_domain_status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-domain-status'), 'ext_domain_status', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_ext_domain_status', pyxb.binding.datatypes.string)
    __ext_domain_status._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1241, 6)
    __ext_domain_status._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1241, 6)
    
    ext_domain_status = property(__ext_domain_status.value, __ext_domain_status.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_44_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1243, 6)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1243, 6)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __Name.name() : __Name,
        __DateDomainWasChecked.name() : __DateDomainWasChecked,
        __RegistrationDate.name() : __RegistrationDate,
        __ExpirationDate.name() : __ExpirationDate,
        __RelatedDNS.name() : __RelatedDNS,
        __Nameservers.name() : __Nameservers,
        __DomainContacts.name() : __DomainContacts
    })
    _AttributeMap.update({
        __system_status.name() : __system_status,
        __ext_system_status.name() : __ext_system_status,
        __domain_status.name() : __domain_status,
        __ext_domain_status.name() : __ext_domain_status,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1281, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute record-type uses Python identifier record_type
    __record_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'record-type'), 'record_type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_45_record_type', STD_ANON_2)
    __record_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1284, 6)
    __record_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1284, 6)
    
    record_type = property(__record_type.value, __record_type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __record_type.name() : __record_type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1361, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RecordData uses Python identifier RecordData
    __RecordData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), 'RecordData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_46_urnietfparamsxmlnsiodef_2_0RecordData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1372, 4), )

    
    RecordData = property(__RecordData.value, __RecordData.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_46_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1366, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1366, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_46_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1368, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1368, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __RecordData.name() : __RecordData
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1373, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0AdditionalData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DateTime uses Python identifier DateTime
    __DateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), 'DateTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0DateTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 397, 4), )

    
    DateTime = property(__DateTime.value, __DateTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RecordPattern uses Python identifier RecordPattern
    __RecordPattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), 'RecordPattern', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0RecordPattern', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1403, 4), )

    
    RecordPattern = property(__RecordPattern.value, __RecordPattern.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RecordItem uses Python identifier RecordItem
    __RecordItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), 'RecordItem', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0RecordItem', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1443, 4), )

    
    RecordItem = property(__RecordItem.value, __RecordItem.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}WindowsRegistryKeysModified uses Python identifier WindowsRegistryKeysModified
    __WindowsRegistryKeysModified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'WindowsRegistryKeysModified'), 'WindowsRegistryKeysModified', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0WindowsRegistryKeysModified', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1450, 4), )

    
    WindowsRegistryKeysModified = property(__WindowsRegistryKeysModified.value, __WindowsRegistryKeysModified.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}FileData uses Python identifier FileData
    __FileData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileData'), 'FileData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0FileData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1495, 3), )

    
    FileData = property(__FileData.value, __FileData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}CertificateData uses Python identifier CertificateData
    __CertificateData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CertificateData'), 'CertificateData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0CertificateData', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1619, 2), )

    
    CertificateData = property(__CertificateData.value, __CertificateData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Application uses Python identifier Application
    __Application = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Application'), 'Application', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0Application', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4), )

    
    Application = property(__Application.value, __Application.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1394, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1394, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1396, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1396, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_47_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1398, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1398, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _ElementMap.update({
        __AdditionalData.name() : __AdditionalData,
        __DateTime.name() : __DateTime,
        __RecordPattern.name() : __RecordPattern,
        __RecordItem.name() : __RecordItem,
        __WindowsRegistryKeysModified.name() : __WindowsRegistryKeysModified,
        __FileData.name() : __FileData,
        __CertificateData.name() : __CertificateData,
        __Application.name() : __Application,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction,
        __observable_id.name() : __observable_id
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_48 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1404, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_48_type', recordpattern_type_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1407, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1407, 12)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_48_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1410, 12)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1410, 12)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'offset'), 'offset', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_48_offset', pyxb.binding.datatypes.integer)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1412, 12)
    __offset._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1412, 12)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute offsetunit uses Python identifier offsetunit
    __offsetunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'offsetunit'), 'offsetunit', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_48_offsetunit', recordpattern_offsetunit_type, unicode_default=u'line')
    __offsetunit._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1414, 12)
    __offsetunit._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1414, 12)
    
    offsetunit = property(__offsetunit.value, __offsetunit.set, None, None)

    
    # Attribute ext-offsetunit uses Python identifier ext_offsetunit
    __ext_offsetunit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-offsetunit'), 'ext_offsetunit', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_48_ext_offsetunit', pyxb.binding.datatypes.string)
    __ext_offsetunit._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1417, 12)
    __ext_offsetunit._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1417, 12)
    
    ext_offsetunit = property(__ext_offsetunit.value, __ext_offsetunit.set, None, None)

    
    # Attribute instance uses Python identifier instance
    __instance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instance'), 'instance', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_48_instance', pyxb.binding.datatypes.integer)
    __instance._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1419, 12)
    __instance._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1419, 12)
    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_49 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1462, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}KeyName uses Python identifier KeyName
    __KeyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'KeyName'), 'KeyName', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_49_urnietfparamsxmlnsiodef_2_0KeyName', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1474, 5), )

    
    KeyName = property(__KeyName.value, __KeyName.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_49_urnietfparamsxmlnsiodef_2_0Value', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1475, 5), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute registryaction uses Python identifier registryaction
    __registryaction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'registryaction'), 'registryaction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_49_registryaction', key_registryaction_type)
    __registryaction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1467, 9)
    __registryaction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1467, 9)
    
    registryaction = property(__registryaction.value, __registryaction.set, None, None)

    
    # Attribute ext-registryaction uses Python identifier ext_registryaction
    __ext_registryaction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-registryaction'), 'ext_registryaction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_49_ext_registryaction', pyxb.binding.datatypes.string)
    __ext_registryaction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1469, 9)
    __ext_registryaction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1469, 9)
    
    ext_registryaction = property(__ext_registryaction.value, __ext_registryaction.set, None, None)

    _ElementMap.update({
        __KeyName.name() : __KeyName,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        __registryaction.name() : __registryaction,
        __ext_registryaction.name() : __ext_registryaction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_50 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1496, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}File uses Python identifier File
    __File = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'File'), 'File', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_50_urnietfparamsxmlnsiodef_2_0File', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1510, 3), )

    
    File = property(__File.value, __File.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_50_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1501, 8)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1501, 8)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_50_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1503, 8)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1503, 8)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_50_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1505, 8)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1505, 8)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __File.name() : __File
    })
    _AttributeMap.update({
        __observable_id.name() : __observable_id,
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_51 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1544, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}HashTarget uses Python identifier HashTarget
    __HashTarget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HashTarget'), 'HashTarget', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_51_urnietfparamsxmlnsiodef_2_0HashTarget', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1560, 2), )

    
    HashTarget = property(__HashTarget.value, __HashTarget.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Hash uses Python identifier Hash
    __Hash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Hash'), 'Hash', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_51_urnietfparamsxmlnsiodef_2_0Hash', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1576, 2), )

    
    Hash = property(__Hash.value, __Hash.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}FuzzyHash uses Python identifier FuzzyHash
    __FuzzyHash = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FuzzyHash'), 'FuzzyHash', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_51_urnietfparamsxmlnsiodef_2_0FuzzyHash', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1588, 2), )

    
    FuzzyHash = property(__FuzzyHash.value, __FuzzyHash.set, None, None)

    
    # Attribute scope uses Python identifier scope
    __scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scope'), 'scope', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_51_scope', hashdata_scope_type, required=True)
    __scope._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1552, 6)
    __scope._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1552, 6)
    
    scope = property(__scope.value, __scope.set, None, None)

    
    # Attribute ext-scope uses Python identifier ext_scope
    __ext_scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-scope'), 'ext_scope', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_51_ext_scope', pyxb.binding.datatypes.string)
    __ext_scope._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1555, 6)
    __ext_scope._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1555, 6)
    
    ext_scope = property(__ext_scope.value, __ext_scope.set, None, None)

    _ElementMap.update({
        __HashTarget.name() : __HashTarget,
        __Hash.name() : __Hash,
        __FuzzyHash.name() : __FuzzyHash
    })
    _AttributeMap.update({
        __scope.name() : __scope,
        __ext_scope.name() : __ext_scope
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_52 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1620, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Certificate uses Python identifier Certificate
    __Certificate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Certificate'), 'Certificate', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_52_urnietfparamsxmlnsiodef_2_0Certificate', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1634, 2), )

    
    Certificate = property(__Certificate.value, __Certificate.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_52_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1625, 6)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1625, 6)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_52_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1627, 6)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1627, 6)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_52_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1629, 6)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1629, 6)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __Certificate.name() : __Certificate
    })
    _AttributeMap.update({
        __observable_id.name() : __observable_id,
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_53 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1661, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute spec-name uses Python identifier spec_name
    __spec_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'spec-name'), 'spec_name', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_53_spec_name', softwarereference_spec_name_type, required=True)
    __spec_name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1666, 8)
    __spec_name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1666, 8)
    
    spec_name = property(__spec_name.value, __spec_name.set, None, None)

    
    # Attribute ext-spec-name uses Python identifier ext_spec_name
    __ext_spec_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-spec-name'), 'ext_spec_name', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_53_ext_spec_name', pyxb.binding.datatypes.string)
    __ext_spec_name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1669, 8)
    __ext_spec_name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1669, 8)
    
    ext_spec_name = property(__ext_spec_name.value, __ext_spec_name.set, None, None)

    
    # Attribute dtype uses Python identifier dtype
    __dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dtype'), 'dtype', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_53_dtype', softwarereference_dtype_type)
    __dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1671, 8)
    __dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1671, 8)
    
    dtype = property(__dtype.value, __dtype.set, None, None)

    
    # Attribute ext-dtype uses Python identifier ext_dtype
    __ext_dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-dtype'), 'ext_dtype', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_53_ext_dtype', pyxb.binding.datatypes.string)
    __ext_dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1674, 8)
    __ext_dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1674, 8)
    
    ext_dtype = property(__ext_dtype.value, __ext_dtype.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __spec_name.name() : __spec_name,
        __ext_spec_name.name() : __ext_spec_name,
        __dtype.name() : __dtype,
        __ext_dtype.name() : __ext_dtype
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_54 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1717, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Contact uses Python identifier Contact
    __Contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Contact'), 'Contact', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0Contact', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4), )

    
    Contact = property(__Contact.value, __Contact.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), 'StartTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0StartTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EndTime uses Python identifier EndTime
    __EndTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), 'EndTime', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0EndTime', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4), )

    
    EndTime = property(__EndTime.value, __EndTime.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Confidence uses Python identifier Confidence
    __Confidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), 'Confidence', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0Confidence', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 797, 4), )

    
    Confidence = property(__Confidence.value, __Confidence.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IndicatorID uses Python identifier IndicatorID
    __IndicatorID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IndicatorID'), 'IndicatorID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0IndicatorID', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1746, 3), )

    
    IndicatorID = property(__IndicatorID.value, __IndicatorID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AlternativeIndicatorID uses Python identifier AlternativeIndicatorID
    __AlternativeIndicatorID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AlternativeIndicatorID'), 'AlternativeIndicatorID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0AlternativeIndicatorID', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1759, 3), )

    
    AlternativeIndicatorID = property(__AlternativeIndicatorID.value, __AlternativeIndicatorID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Observable uses Python identifier Observable
    __Observable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Observable'), 'Observable', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0Observable', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1772, 3), )

    
    Observable = property(__Observable.value, __Observable.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IndicatorExpression uses Python identifier IndicatorExpression
    __IndicatorExpression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IndicatorExpression'), 'IndicatorExpression', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0IndicatorExpression', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1877, 3), )

    
    IndicatorExpression = property(__IndicatorExpression.value, __IndicatorExpression.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ObservableReference uses Python identifier ObservableReference
    __ObservableReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ObservableReference'), 'ObservableReference', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0ObservableReference', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1909, 3), )

    
    ObservableReference = property(__ObservableReference.value, __ObservableReference.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IndicatorReference uses Python identifier IndicatorReference
    __IndicatorReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IndicatorReference'), 'IndicatorReference', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0IndicatorReference', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1916, 3), )

    
    IndicatorReference = property(__IndicatorReference.value, __IndicatorReference.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_urnietfparamsxmlnsiodef_2_0Description', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1739, 7)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1739, 7)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_54_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1741, 7)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1741, 7)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __Contact.name() : __Contact,
        __StartTime.name() : __StartTime,
        __EndTime.name() : __EndTime,
        __Confidence.name() : __Confidence,
        __IndicatorID.name() : __IndicatorID,
        __AlternativeIndicatorID.name() : __AlternativeIndicatorID,
        __Observable.name() : __Observable,
        __IndicatorExpression.name() : __IndicatorExpression,
        __ObservableReference.name() : __ObservableReference,
        __IndicatorReference.name() : __IndicatorReference,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_55 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1760, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IndicatorID uses Python identifier IndicatorID
    __IndicatorID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IndicatorID'), 'IndicatorID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_55_urnietfparamsxmlnsiodef_2_0IndicatorID', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1746, 3), )

    
    IndicatorID = property(__IndicatorID.value, __IndicatorID.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_55_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1765, 7)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1765, 7)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_55_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1767, 7)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1767, 7)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __IndicatorID.name() : __IndicatorID
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_56 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1773, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Incident uses Python identifier Incident
    __Incident = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Incident'), 'Incident', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0Incident', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 50, 4), )

    
    Incident = property(__Incident.value, __Incident.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AdditionalData uses Python identifier AdditionalData
    __AdditionalData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), 'AdditionalData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0AdditionalData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4), )

    
    AdditionalData = property(__AdditionalData.value, __AdditionalData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RegistryHandle uses Python identifier RegistryHandle
    __RegistryHandle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), 'RegistryHandle', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0RegistryHandle', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 343, 4), )

    
    RegistryHandle = property(__RegistryHandle.value, __RegistryHandle.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}HistoryItem uses Python identifier HistoryItem
    __HistoryItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), 'HistoryItem', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0HistoryItem', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 436, 4), )

    
    HistoryItem = property(__HistoryItem.value, __HistoryItem.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Expectation uses Python identifier Expectation
    __Expectation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), 'Expectation', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0Expectation', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 470, 4), )

    
    Expectation = property(__Expectation.value, __Expectation.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Reference'), 'Reference', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0Reference', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 596, 4), )

    
    Reference = property(__Reference.value, __Reference.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Assessment uses Python identifier Assessment
    __Assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), 'Assessment', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0Assessment', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 616, 4), )

    
    Assessment = property(__Assessment.value, __Assessment.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EventData uses Python identifier EventData
    __EventData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EventData'), 'EventData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0EventData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 819, 4), )

    
    EventData = property(__EventData.value, __EventData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0Address', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 967, 4), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}EmailData uses Python identifier EmailData
    __EmailData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EmailData'), 'EmailData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0EmailData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1190, 3), )

    
    EmailData = property(__EmailData.value, __EmailData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}DomainData uses Python identifier DomainData
    __DomainData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DomainData'), 'DomainData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0DomainData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1218, 2), )

    
    DomainData = property(__DomainData.value, __DomainData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}RecordData uses Python identifier RecordData
    __RecordData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), 'RecordData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0RecordData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1372, 4), )

    
    RecordData = property(__RecordData.value, __RecordData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}WindowsRegistryKeysModified uses Python identifier WindowsRegistryKeysModified
    __WindowsRegistryKeysModified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'WindowsRegistryKeysModified'), 'WindowsRegistryKeysModified', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0WindowsRegistryKeysModified', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1450, 4), )

    
    WindowsRegistryKeysModified = property(__WindowsRegistryKeysModified.value, __WindowsRegistryKeysModified.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}FileData uses Python identifier FileData
    __FileData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'FileData'), 'FileData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0FileData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1495, 3), )

    
    FileData = property(__FileData.value, __FileData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}CertificateData uses Python identifier CertificateData
    __CertificateData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'CertificateData'), 'CertificateData', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0CertificateData', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1619, 2), )

    
    CertificateData = property(__CertificateData.value, __CertificateData.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ApplicationHeader uses Python identifier ApplicationHeader
    __ApplicationHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeader'), 'ApplicationHeader', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0ApplicationHeader', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1781, 9), )

    
    ApplicationHeader = property(__ApplicationHeader.value, __ApplicationHeader.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}BulkObservable uses Python identifier BulkObservable
    __BulkObservable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'BulkObservable'), 'BulkObservable', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_urnietfparamsxmlnsiodef_2_0BulkObservable', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1818, 3), )

    
    BulkObservable = property(__BulkObservable.value, __BulkObservable.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1811, 7)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1811, 7)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_56_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1813, 7)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1813, 7)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _ElementMap.update({
        __Incident.name() : __Incident,
        __AdditionalData.name() : __AdditionalData,
        __RegistryHandle.name() : __RegistryHandle,
        __HistoryItem.name() : __HistoryItem,
        __Expectation.name() : __Expectation,
        __Reference.name() : __Reference,
        __Assessment.name() : __Assessment,
        __EventData.name() : __EventData,
        __Address.name() : __Address,
        __EmailData.name() : __EmailData,
        __DomainData.name() : __DomainData,
        __RecordData.name() : __RecordData,
        __WindowsRegistryKeysModified.name() : __WindowsRegistryKeysModified,
        __FileData.name() : __FileData,
        __CertificateData.name() : __CertificateData,
        __ApplicationHeader.name() : __ApplicationHeader,
        __BulkObservable.name() : __BulkObservable
    })
    _AttributeMap.update({
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_57 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1819, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}BulkObservableList uses Python identifier BulkObservableList
    __BulkObservableList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'BulkObservableList'), 'BulkObservableList', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_57_urnietfparamsxmlnsiodef_2_0BulkObservableList', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1823, 9), )

    
    BulkObservableList = property(__BulkObservableList.value, __BulkObservableList.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}BulkObservableFormat uses Python identifier BulkObservableFormat
    __BulkObservableFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'BulkObservableFormat'), 'BulkObservableFormat', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_57_urnietfparamsxmlnsiodef_2_0BulkObservableFormat', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1866, 3), )

    
    BulkObservableFormat = property(__BulkObservableFormat.value, __BulkObservableFormat.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_57_type', observable_type_type, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1826, 7)
    __type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1826, 7)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ext-type uses Python identifier ext_type
    __ext_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-type'), 'ext_type', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_57_ext_type', pyxb.binding.datatypes.string)
    __ext_type._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1829, 7)
    __ext_type._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1829, 7)
    
    ext_type = property(__ext_type.value, __ext_type.set, None, None)

    _ElementMap.update({
        __BulkObservableList.name() : __BulkObservableList,
        __BulkObservableFormat.name() : __BulkObservableFormat
    })
    _AttributeMap.update({
        __type.name() : __type,
        __ext_type.name() : __ext_type
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_58 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1878, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}AlternativeIndicatorID uses Python identifier AlternativeIndicatorID
    __AlternativeIndicatorID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AlternativeIndicatorID'), 'AlternativeIndicatorID', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_58_urnietfparamsxmlnsiodef_2_0AlternativeIndicatorID', True, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1759, 3), )

    
    AlternativeIndicatorID = property(__AlternativeIndicatorID.value, __AlternativeIndicatorID.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}Observable uses Python identifier Observable
    __Observable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Observable'), 'Observable', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_58_urnietfparamsxmlnsiodef_2_0Observable', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1772, 3), )

    
    Observable = property(__Observable.value, __Observable.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IndicatorExpression uses Python identifier IndicatorExpression
    __IndicatorExpression = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IndicatorExpression'), 'IndicatorExpression', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_58_urnietfparamsxmlnsiodef_2_0IndicatorExpression', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1877, 3), )

    
    IndicatorExpression = property(__IndicatorExpression.value, __IndicatorExpression.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}ObservableReference uses Python identifier ObservableReference
    __ObservableReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ObservableReference'), 'ObservableReference', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_58_urnietfparamsxmlnsiodef_2_0ObservableReference', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1909, 3), )

    
    ObservableReference = property(__ObservableReference.value, __ObservableReference.set, None, None)

    
    # Element {urn:ietf:params:xml:ns:iodef-2.0}IndicatorReference uses Python identifier IndicatorReference
    __IndicatorReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IndicatorReference'), 'IndicatorReference', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_58_urnietfparamsxmlnsiodef_2_0IndicatorReference', False, pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1916, 3), )

    
    IndicatorReference = property(__IndicatorReference.value, __IndicatorReference.set, None, None)

    
    # Attribute operator uses Python identifier operator
    __operator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'operator'), 'operator', '__urnietfparamsxmlnsiodef_2_0_CTD_ANON_58_operator', indicatorexpression_operator_type, required=True)
    __operator._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1893, 7)
    __operator._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1893, 7)
    
    operator = property(__operator.value, __operator.set, None, None)

    _ElementMap.update({
        __AlternativeIndicatorID.name() : __AlternativeIndicatorID,
        __Observable.name() : __Observable,
        __IndicatorExpression.name() : __IndicatorExpression,
        __ObservableReference.name() : __ObservableReference,
        __IndicatorReference.name() : __IndicatorReference
    })
    _AttributeMap.update({
        __operator.name() : __operator
    })



# Complex type {urn:ietf:params:xml:ns:iodef-2.0}ExtensionType with content type MIXED
class ExtensionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-2.0}ExtensionType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExtensionType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1960, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute dtype uses Python identifier dtype
    __dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dtype'), 'dtype', '__urnietfparamsxmlnsiodef_2_0_ExtensionType_dtype', dtype_type, required=True)
    __dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1965, 6)
    __dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1965, 6)
    
    dtype = property(__dtype.value, __dtype.set, None, None)

    
    # Attribute meaning uses Python identifier meaning
    __meaning = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'meaning'), 'meaning', '__urnietfparamsxmlnsiodef_2_0_ExtensionType_meaning', pyxb.binding.datatypes.string)
    __meaning._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1967, 6)
    __meaning._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1967, 6)
    
    meaning = property(__meaning.value, __meaning.set, None, None)

    
    # Attribute formatid uses Python identifier formatid
    __formatid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatid'), 'formatid', '__urnietfparamsxmlnsiodef_2_0_ExtensionType_formatid', pyxb.binding.datatypes.string)
    __formatid._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1969, 6)
    __formatid._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1969, 6)
    
    formatid = property(__formatid.value, __formatid.set, None, None)

    
    # Attribute restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restriction'), 'restriction', '__urnietfparamsxmlnsiodef_2_0_ExtensionType_restriction', restriction_type)
    __restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1971, 6)
    __restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1971, 6)
    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute ext-restriction uses Python identifier ext_restriction
    __ext_restriction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ext-restriction'), 'ext_restriction', '__urnietfparamsxmlnsiodef_2_0_ExtensionType_ext_restriction', pyxb.binding.datatypes.string)
    __ext_restriction._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1973, 6)
    __ext_restriction._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1973, 6)
    
    ext_restriction = property(__ext_restriction.value, __ext_restriction.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __dtype.name() : __dtype,
        __meaning.name() : __meaning,
        __formatid.name() : __formatid,
        __restriction.name() : __restriction,
        __ext_restriction.name() : __ext_restriction
    })
Namespace.addCategoryObject('typeBinding', u'ExtensionType', ExtensionType)


# Complex type {urn:ietf:params:xml:ns:iodef-2.0}ApplicationHeaderType with content type MIXED
class ApplicationHeaderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:ietf:params:xml:ns:iodef-2.0}ApplicationHeaderType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeaderType')
    _XSDLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1977, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute proto uses Python identifier proto
    __proto = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'proto'), 'proto', '__urnietfparamsxmlnsiodef_2_0_ApplicationHeaderType_proto', pyxb.binding.datatypes.integer)
    __proto._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1982, 6)
    __proto._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1982, 6)
    
    proto = property(__proto.value, __proto.set, None, None)

    
    # Attribute proto-name uses Python identifier proto_name
    __proto_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'proto-name'), 'proto_name', '__urnietfparamsxmlnsiodef_2_0_ApplicationHeaderType_proto_name', pyxb.binding.datatypes.integer)
    __proto_name._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1984, 6)
    __proto_name._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1984, 6)
    
    proto_name = property(__proto_name.value, __proto_name.set, None, None)

    
    # Attribute field uses Python identifier field
    __field = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'field'), 'field', '__urnietfparamsxmlnsiodef_2_0_ApplicationHeaderType_field', pyxb.binding.datatypes.string, required=True)
    __field._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1986, 6)
    __field._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1986, 6)
    
    field = property(__field.value, __field.set, None, None)

    
    # Attribute dtype uses Python identifier dtype
    __dtype = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dtype'), 'dtype', '__urnietfparamsxmlnsiodef_2_0_ApplicationHeaderType_dtype', proto_dtype_type, required=True)
    __dtype._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1988, 6)
    __dtype._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1988, 6)
    
    dtype = property(__dtype.value, __dtype.set, None, None)

    
    # Attribute observable-id uses Python identifier observable_id
    __observable_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'observable-id'), 'observable_id', '__urnietfparamsxmlnsiodef_2_0_ApplicationHeaderType_observable_id', pyxb.binding.datatypes.ID)
    __observable_id._DeclarationLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1991, 6)
    __observable_id._UseLocation = pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1991, 6)
    
    observable_id = property(__observable_id.value, __observable_id.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __proto.name() : __proto,
        __proto_name.name() : __proto_name,
        __field.name() : __field,
        __dtype.name() : __dtype,
        __observable_id.name() : __observable_id
    })
Namespace.addCategoryObject('typeBinding', u'ApplicationHeaderType', ApplicationHeaderType)


ThreatActorID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThreatActorID'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 224, 4))
Namespace.addCategoryObject('elementBinding', ThreatActorID.name().localName(), ThreatActorID)

CampaignID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CampaignID'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 252, 4))
Namespace.addCategoryObject('elementBinding', CampaignID.name().localName(), CampaignID)

DateTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 397, 4))
Namespace.addCategoryObject('elementBinding', DateTime.name().localName(), DateTime)

ReportTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 399, 4))
Namespace.addCategoryObject('elementBinding', ReportTime.name().localName(), ReportTime)

DetectTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 401, 4))
Namespace.addCategoryObject('elementBinding', DetectTime.name().localName(), DetectTime)

StartTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4))
Namespace.addCategoryObject('elementBinding', StartTime.name().localName(), StartTime)

EndTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4))
Namespace.addCategoryObject('elementBinding', EndTime.name().localName(), EndTime)

RecoveryTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecoveryTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 407, 4))
Namespace.addCategoryObject('elementBinding', RecoveryTime.name().localName(), RecoveryTime)

GenerationTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GenerationTime'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 409, 4))
Namespace.addCategoryObject('elementBinding', GenerationTime.name().localName(), GenerationTime)

Port = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Port'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1109, 4))
Namespace.addCategoryObject('elementBinding', Port.name().localName(), Port)

ProtoType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoType'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1111, 4))
Namespace.addCategoryObject('elementBinding', ProtoType.name().localName(), ProtoType)

ProtoCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1112, 4))
Namespace.addCategoryObject('elementBinding', ProtoCode.name().localName(), ProtoCode)

ProtoField = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoField'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1113, 4))
Namespace.addCategoryObject('elementBinding', ProtoField.name().localName(), ProtoField)

IANAService = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IANAService'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1129, 4))
Namespace.addCategoryObject('elementBinding', IANAService.name().localName(), IANAService)

Name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1248, 2))
Namespace.addCategoryObject('elementBinding', Name.name().localName(), Name)

DateDomainWasChecked = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateDomainWasChecked'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1249, 2))
Namespace.addCategoryObject('elementBinding', DateDomainWasChecked.name().localName(), DateDomainWasChecked)

RegistrationDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistrationDate'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1250, 2))
Namespace.addCategoryObject('elementBinding', RegistrationDate.name().localName(), RegistrationDate)

ExpirationDate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpirationDate'), pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1251, 2))
Namespace.addCategoryObject('elementBinding', ExpirationDate.name().localName(), ExpirationDate)

Server = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Server'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1341, 3))
Namespace.addCategoryObject('elementBinding', Server.name().localName(), Server)

SameDomainContact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SameDomainContact'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1353, 3))
Namespace.addCategoryObject('elementBinding', SameDomainContact.name().localName(), SameDomainContact)

KeyName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KeyName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1474, 5))
Namespace.addCategoryObject('elementBinding', KeyName.name().localName(), KeyName)

Value = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1475, 5))
Namespace.addCategoryObject('elementBinding', Value.name().localName(), Value)

FileName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileName'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1532, 3))
Namespace.addCategoryObject('elementBinding', FileName.name().localName(), FileName)

FileSize = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileSize'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1533, 3))
Namespace.addCategoryObject('elementBinding', FileSize.name().localName(), FileSize)

FileType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileType'), pyxb.binding.datatypes.integer, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1534, 3))
Namespace.addCategoryObject('elementBinding', FileType.name().localName(), FileType)

URL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4))
Namespace.addCategoryObject('elementBinding', URL.name().localName(), URL)

IODEF_Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IODEF-Document'), CTD_ANON, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 26, 4))
Namespace.addCategoryObject('elementBinding', IODEF_Document.name().localName(), IODEF_Document)

ContactName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 339, 4))
Namespace.addCategoryObject('elementBinding', ContactName.name().localName(), ContactName)

ContactTitle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactTitle'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 341, 4))
Namespace.addCategoryObject('elementBinding', ContactTitle.name().localName(), ContactTitle)

Email = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Email'), ContactMeansType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 379, 4))
Namespace.addCategoryObject('elementBinding', Email.name().localName(), Email)

Telephone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), ContactMeansType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 380, 4))
Namespace.addCategoryObject('elementBinding', Telephone.name().localName(), Telephone)

Fax = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), ContactMeansType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 381, 4))
Namespace.addCategoryObject('elementBinding', Fax.name().localName(), Fax)

Timezone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), TimezoneType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 411, 4))
Namespace.addCategoryObject('elementBinding', Timezone.name().localName(), Timezone)

DefinedCOA = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DefinedCOA'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 463, 4))
Namespace.addCategoryObject('elementBinding', DefinedCOA.name().localName(), DefinedCOA)

Reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), CTD_ANON_, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 596, 4))
Namespace.addCategoryObject('elementBinding', Reference.name().localName(), Reference)

IncidentCategory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentCategory'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 653, 4))
Namespace.addCategoryObject('elementBinding', IncidentCategory.name().localName(), IncidentCategory)

MitigatingFactor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MitigatingFactor'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 658, 4))
Namespace.addCategoryObject('elementBinding', MitigatingFactor.name().localName(), MitigatingFactor)

Flow = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flow'), CTD_ANON_2, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 867, 4))
Namespace.addCategoryObject('elementBinding', Flow.name().localName(), Flow)

Node = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Node'), CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 947, 4))
Namespace.addCategoryObject('elementBinding', Node.name().localName(), Node)

Location = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1004, 4))
Namespace.addCategoryObject('elementBinding', Location.name().localName(), Location)

Service = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Service'), CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1084, 4))
Namespace.addCategoryObject('elementBinding', Service.name().localName(), Service)

Portlist = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Portlist'), PortlistType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1110, 4))
Namespace.addCategoryObject('elementBinding', Portlist.name().localName(), Portlist)

ServiceName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceName'), CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1117, 4))
Namespace.addCategoryObject('elementBinding', ServiceName.name().localName(), ServiceName)

EmailData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailData'), CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1190, 3))
Namespace.addCategoryObject('elementBinding', EmailData.name().localName(), EmailData)

EmailFrom = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailFrom'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1207, 3))
Namespace.addCategoryObject('elementBinding', EmailFrom.name().localName(), EmailFrom)

EmailSubject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailSubject'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1208, 3))
Namespace.addCategoryObject('elementBinding', EmailSubject.name().localName(), EmailSubject)

EmailX_Mailer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailX-Mailer'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1209, 3))
Namespace.addCategoryObject('elementBinding', EmailX_Mailer.name().localName(), EmailX_Mailer)

Nameservers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nameservers'), CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1332, 3))
Namespace.addCategoryObject('elementBinding', Nameservers.name().localName(), Nameservers)

DomainContacts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DomainContacts'), CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1343, 3))
Namespace.addCategoryObject('elementBinding', DomainContacts.name().localName(), DomainContacts)

WindowsRegistryKeysModified = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WindowsRegistryKeysModified'), CTD_ANON_9, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1450, 4))
Namespace.addCategoryObject('elementBinding', WindowsRegistryKeysModified.name().localName(), WindowsRegistryKeysModified)

File = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'File'), CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1510, 3))
Namespace.addCategoryObject('elementBinding', File.name().localName(), File)

HashTarget = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HashTarget'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1560, 2))
Namespace.addCategoryObject('elementBinding', HashTarget.name().localName(), HashTarget)

Hash = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hash'), CTD_ANON_11, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1576, 2))
Namespace.addCategoryObject('elementBinding', Hash.name().localName(), Hash)

FuzzyHash = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FuzzyHash'), CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1588, 2))
Namespace.addCategoryObject('elementBinding', FuzzyHash.name().localName(), FuzzyHash)

SignatureData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignatureData'), CTD_ANON_13, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1604, 2))
Namespace.addCategoryObject('elementBinding', SignatureData.name().localName(), SignatureData)

Certificate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Certificate'), CTD_ANON_14, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1634, 2))
Namespace.addCategoryObject('elementBinding', Certificate.name().localName(), Certificate)

Application = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4))
Namespace.addCategoryObject('elementBinding', Application.name().localName(), Application)

OperatingSystem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1700, 4))
Namespace.addCategoryObject('elementBinding', OperatingSystem.name().localName(), OperatingSystem)

IndicatorData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorData'), CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1707, 3))
Namespace.addCategoryObject('elementBinding', IndicatorData.name().localName(), IndicatorData)

IndicatorID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorID'), CTD_ANON_16, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1746, 3))
Namespace.addCategoryObject('elementBinding', IndicatorID.name().localName(), IndicatorID)

BulkObservableFormat = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BulkObservableFormat'), CTD_ANON_17, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1866, 3))
Namespace.addCategoryObject('elementBinding', BulkObservableFormat.name().localName(), BulkObservableFormat)

ObservableReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservableReference'), CTD_ANON_18, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1909, 3))
Namespace.addCategoryObject('elementBinding', ObservableReference.name().localName(), ObservableReference)

IndicatorReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorReference'), CTD_ANON_19, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1916, 3))
Namespace.addCategoryObject('elementBinding', IndicatorReference.name().localName(), IndicatorReference)

Description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4))
Namespace.addCategoryObject('elementBinding', Description.name().localName(), Description)

Incident = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Incident'), CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 50, 4))
Namespace.addCategoryObject('elementBinding', Incident.name().localName(), Incident)

IncidentID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4))
Namespace.addCategoryObject('elementBinding', IncidentID.name().localName(), IncidentID)

AlternativeID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 153, 4))
Namespace.addCategoryObject('elementBinding', AlternativeID.name().localName(), AlternativeID)

RelatedActivity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 170, 4))
Namespace.addCategoryObject('elementBinding', RelatedActivity.name().localName(), RelatedActivity)

ThreatActor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThreatActor'), CTD_ANON_23, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 202, 4))
Namespace.addCategoryObject('elementBinding', ThreatActor.name().localName(), ThreatActor)

Campaign = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Campaign'), CTD_ANON_24, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 231, 4))
Namespace.addCategoryObject('elementBinding', Campaign.name().localName(), Campaign)

AdditionalData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4))
Namespace.addCategoryObject('elementBinding', AdditionalData.name().localName(), AdditionalData)

Contact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4))
Namespace.addCategoryObject('elementBinding', Contact.name().localName(), Contact)

RegistryHandle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), CTD_ANON_26, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 343, 4))
Namespace.addCategoryObject('elementBinding', RegistryHandle.name().localName(), RegistryHandle)

PostalAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), CTD_ANON_27, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 369, 4))
Namespace.addCategoryObject('elementBinding', PostalAddress.name().localName(), PostalAddress)

History = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'History'), CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 423, 4))
Namespace.addCategoryObject('elementBinding', History.name().localName(), History)

HistoryItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), CTD_ANON_29, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 436, 4))
Namespace.addCategoryObject('elementBinding', HistoryItem.name().localName(), HistoryItem)

Expectation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), CTD_ANON_30, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 470, 4))
Namespace.addCategoryObject('elementBinding', Expectation.name().localName(), Expectation)

Discovery = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Discovery'), CTD_ANON_31, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 505, 4))
Namespace.addCategoryObject('elementBinding', Discovery.name().localName(), Discovery)

DetectionPattern = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionPattern'), CTD_ANON_32, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 552, 4))
Namespace.addCategoryObject('elementBinding', DetectionPattern.name().localName(), DetectionPattern)

Method = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Method'), CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 574, 4))
Namespace.addCategoryObject('elementBinding', Method.name().localName(), Method)

Assessment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 616, 4))
Namespace.addCategoryObject('elementBinding', Assessment.name().localName(), Assessment)

BusinessImpact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BusinessImpact'), BusinessImpactType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 654, 4))
Namespace.addCategoryObject('elementBinding', BusinessImpact.name().localName(), BusinessImpact)

IntendedImpact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IntendedImpact'), BusinessImpactType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 656, 4))
Namespace.addCategoryObject('elementBinding', IntendedImpact.name().localName(), IntendedImpact)

SystemImpact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SystemImpact'), CTD_ANON_35, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 661, 4))
Namespace.addCategoryObject('elementBinding', SystemImpact.name().localName(), SystemImpact)

TimeImpact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), CTD_ANON_36, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 760, 4))
Namespace.addCategoryObject('elementBinding', TimeImpact.name().localName(), TimeImpact)

MonetaryImpact = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), CTD_ANON_37, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 784, 4))
Namespace.addCategoryObject('elementBinding', MonetaryImpact.name().localName(), MonetaryImpact)

Confidence = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), CTD_ANON_38, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 797, 4))
Namespace.addCategoryObject('elementBinding', Confidence.name().localName(), Confidence)

EventData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 819, 4))
Namespace.addCategoryObject('elementBinding', EventData.name().localName(), EventData)

System = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'System'), CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 880, 4))
Namespace.addCategoryObject('elementBinding', System.name().localName(), System)

Address = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), CTD_ANON_41, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 967, 4))
Namespace.addCategoryObject('elementBinding', Address.name().localName(), Address)

NodeRole = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), CTD_ANON_42, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1006, 4))
Namespace.addCategoryObject('elementBinding', NodeRole.name().localName(), NodeRole)

ApplicationHeader = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeader'), ApplicationHeaderType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1114, 4))
Namespace.addCategoryObject('elementBinding', ApplicationHeader.name().localName(), ApplicationHeader)

Counter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_43, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1136, 4))
Namespace.addCategoryObject('elementBinding', Counter.name().localName(), Counter)

EmailHeaderField = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailHeaderField'), ApplicationHeaderType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1210, 3))
Namespace.addCategoryObject('elementBinding', EmailHeaderField.name().localName(), EmailHeaderField)

DomainData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DomainData'), CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1218, 2))
Namespace.addCategoryObject('elementBinding', DomainData.name().localName(), DomainData)

RelatedDNS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatedDNS'), CTD_ANON_45, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1280, 2))
Namespace.addCategoryObject('elementBinding', RelatedDNS.name().localName(), RelatedDNS)

Record = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Record'), CTD_ANON_46, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1360, 4))
Namespace.addCategoryObject('elementBinding', Record.name().localName(), Record)

RecordData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1372, 4))
Namespace.addCategoryObject('elementBinding', RecordData.name().localName(), RecordData)

RecordPattern = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), CTD_ANON_48, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1403, 4))
Namespace.addCategoryObject('elementBinding', RecordPattern.name().localName(), RecordPattern)

RecordItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), ExtensionType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1443, 4))
Namespace.addCategoryObject('elementBinding', RecordItem.name().localName(), RecordItem)

Key = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Key'), CTD_ANON_49, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1461, 5))
Namespace.addCategoryObject('elementBinding', Key.name().localName(), Key)

FileData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileData'), CTD_ANON_50, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1495, 3))
Namespace.addCategoryObject('elementBinding', FileData.name().localName(), FileData)

FileProperties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileProperties'), ExtensionType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1535, 3))
Namespace.addCategoryObject('elementBinding', FileProperties.name().localName(), FileProperties)

HashData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HashData'), CTD_ANON_51, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1543, 2))
Namespace.addCategoryObject('elementBinding', HashData.name().localName(), HashData)

CertificateData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CertificateData'), CTD_ANON_52, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1619, 2))
Namespace.addCategoryObject('elementBinding', CertificateData.name().localName(), CertificateData)

SoftwareReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SoftwareReference'), CTD_ANON_53, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1660, 4))
Namespace.addCategoryObject('elementBinding', SoftwareReference.name().localName(), SoftwareReference)

Indicator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Indicator'), CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1716, 3))
Namespace.addCategoryObject('elementBinding', Indicator.name().localName(), Indicator)

AlternativeIndicatorID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeIndicatorID'), CTD_ANON_55, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1759, 3))
Namespace.addCategoryObject('elementBinding', AlternativeIndicatorID.name().localName(), AlternativeIndicatorID)

Observable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Observable'), CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1772, 3))
Namespace.addCategoryObject('elementBinding', Observable.name().localName(), Observable)

BulkObservable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BulkObservable'), CTD_ANON_57, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1818, 3))
Namespace.addCategoryObject('elementBinding', BulkObservable.name().localName(), BulkObservable)

IndicatorExpression = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorExpression'), CTD_ANON_58, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1877, 3))
Namespace.addCategoryObject('elementBinding', IndicatorExpression.name().localName(), IndicatorExpression)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Incident'), CTD_ANON_20, scope=CTD_ANON, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 50, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 31, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Incident')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 29, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 31, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_enum, u'ReferenceName'), _ImportedBinding__enum.CTD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'http://www.iana.org/assignments/xml-registry/schema/iodef-enum-1.0.xsd', 13, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 599, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 601, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 603, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(_Namespace_enum, u'ReferenceName')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 599, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 601, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 603, 10))
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
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'System'), CTD_ANON_40, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 880, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'System')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 870, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), CTD_ANON_27, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 369, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), CTD_ANON_41, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 967, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Location'), MLStringType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1004, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), CTD_ANON_42, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1006, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_43, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1136, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DomainData'), CTD_ANON_44, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1218, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 951, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 953, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 956, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 958, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 960, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 962, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DomainData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 951, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 953, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 956, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Location')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 958, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NodeRole')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 960, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 962, 10))
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




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Port'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1109, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Portlist'), PortlistType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1110, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoType'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1111, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1112, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtoField'), pyxb.binding.datatypes.integer, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1113, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeader'), ApplicationHeaderType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1114, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ServiceName'), CTD_ANON_5, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1117, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailData'), CTD_ANON_6, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1190, 3)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1087, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1089, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1093, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1094, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1095, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1096, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1098, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1099, 10))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ServiceName')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1087, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Port')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1090, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Portlist')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1091, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoType')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1093, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoCode')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1094, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ProtoField')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1095, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeader')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1096, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmailData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1098, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1099, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IANAService'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1129, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1121, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1123, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IANAService')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1120, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1121, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1123, 10))
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
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailFrom'), MLStringType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1207, 3)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailSubject'), MLStringType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1208, 3)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailX-Mailer'), MLStringType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1209, 3)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailHeaderField'), ApplicationHeaderType, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1210, 3)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HashData'), CTD_ANON_51, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1543, 2)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignatureData'), CTD_ANON_13, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1604, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1193, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1194, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1195, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1196, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1197, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1199, 9))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmailFrom')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1193, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmailSubject')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1194, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmailX-Mailer')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1195, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmailHeaderField')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1196, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HashData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1197, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SignatureData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1199, 9))
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
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), CTD_ANON_41, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 967, 4)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Server'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1341, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Server')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1335, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1336, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SameDomainContact'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1353, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SameDomainContact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1346, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1347, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Key'), CTD_ANON_49, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1461, 5)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Key')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1453, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature'), _ImportedBinding__ds.SignatureType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1522, 8)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileName'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1532, 3)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileSize'), pyxb.binding.datatypes.integer, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1533, 3)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileType'), pyxb.binding.datatypes.integer, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1534, 3)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileProperties'), ExtensionType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1535, 3)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HashData'), CTD_ANON_51, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1543, 2)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1513, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1514, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1515, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1516, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1518, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1520, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1522, 8))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1524, 8))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileName')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1513, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileSize')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1514, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileType')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1515, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1516, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HashData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1518, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1520, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1522, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileProperties')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1524, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, u'CanonicalizationMethod'), _ImportedBinding__ds.CanonicalizationMethodType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 75, 2)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, u'DigestMethod'), _ImportedBinding__ds.DigestMethodType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 127, 0)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, u'DigestValue'), _ImportedBinding__ds.DigestValueType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 135, 0)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1582, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'DigestMethod')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1579, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'DigestValue')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1580, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'CanonicalizationMethod')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1581, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1582, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1592, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1591, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1592, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature'), _ImportedBinding__ds.SignatureType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 43, 0)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1607, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, u'X509Data'), _ImportedBinding__ds.X509DataType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd', 183, 0)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'X509Data')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1637, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SoftwareReference'), CTD_ANON_53, scope=SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1660, 4)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

SoftwareType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=SoftwareType, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1651, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1653, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1655, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SoftwareReference')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1651, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1653, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SoftwareType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1655, 8))
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
SoftwareType._Automaton = _BuildAutomaton_15()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Indicator'), CTD_ANON_54, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1716, 3)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Indicator')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1710, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_16()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hash'), CTD_ANON_11, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1576, 2)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1869, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1871, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hash')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1869, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1871, 9))
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
CTD_ANON_17._Automaton = _BuildAutomaton_17()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID'), CTD_ANON_21, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 153, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity'), CTD_ANON_22, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 170, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 399, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 401, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecoveryTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 407, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GenerationTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 409, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'History'), CTD_ANON_28, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 423, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Discovery'), CTD_ANON_31, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 505, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Method'), CTD_ANON_33, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 574, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_34, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 616, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_39, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 819, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 54, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 56, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 58, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 60, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 62, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 64, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 67, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 69, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 71, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 75, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 79, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 81, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 83, 10))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 53, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AlternativeID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 54, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RelatedActivity')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 56, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 58, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 60, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 62, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecoveryTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 64, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReportTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 66, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GenerationTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 67, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 69, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Discovery')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 71, 10))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Assessment')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 73, 10))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Method')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 75, 10))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 77, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 79, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'History')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 81, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 83, 10))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_18()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 156, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_19()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThreatActor'), CTD_ANON_23, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 202, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Campaign'), CTD_ANON_24, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 231, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), CTD_ANON_38, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 797, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1932, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 183, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 185, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 187, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 174, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 176, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ThreatActor')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 178, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Campaign')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 180, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Confidence')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 183, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 185, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 187, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_6, [
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_20()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ThreatActorID'), pyxb.binding.datatypes.string, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 224, 4)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 208, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 214, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ThreatActorID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 207, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 208, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 211, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 214, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_21()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CampaignID'), pyxb.binding.datatypes.string, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 252, 4)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 237, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 243, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CampaignID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 236, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 237, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 240, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 243, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_22()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactName'), MLStringType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 339, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactTitle'), MLStringType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 341, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), CTD_ANON_26, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 343, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress'), CTD_ANON_27, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 369, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Email'), ContactMeansType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 379, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Telephone'), ContactMeansType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 380, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fax'), ContactMeansType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 381, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Timezone'), TimezoneType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 411, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 269, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 271, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 273, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 275, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 277, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 279, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 281, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 283, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 285, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 287, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 289, 10))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactName')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 269, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactTitle')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 271, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 273, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 275, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostalAddress')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 277, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Email')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 279, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Telephone')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 281, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fax')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 283, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Timezone')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 285, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 287, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 289, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_23()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), CTD_ANON_29, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 436, 4)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 426, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_24()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentID'), IncidentIDType, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 131, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 397, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DefinedCOA'), MLStringType, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 463, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 440, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 442, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 444, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 446, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 448, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 439, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 440, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 442, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 444, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DefinedCOA')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 446, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 448, 10))
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
CTD_ANON_29._Automaton = _BuildAutomaton_25()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DefinedCOA'), MLStringType, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 463, 4)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 473, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 475, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 477, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 479, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 481, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 473, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DefinedCOA')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 475, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 477, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 479, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 481, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_26()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionPattern'), CTD_ANON_32, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 552, 4)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 508, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 510, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 512, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 508, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 510, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectionPattern')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 512, 10))
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
CTD_ANON_31._Automaton = _BuildAutomaton_27()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectionConfiguration'), pyxb.binding.datatypes.string, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 558, 10)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 556, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 558, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 555, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 556, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectionConfiguration')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 558, 10))
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
CTD_ANON_32._Automaton = _BuildAutomaton_28()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), CTD_ANON_, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 596, 4)))

CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 581, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 579, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 581, 10))
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
CTD_ANON_33._Automaton = _BuildAutomaton_29()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncidentCategory'), MLStringType, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 653, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BusinessImpact'), BusinessImpactType, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 654, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IntendedImpact'), BusinessImpactType, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 656, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MitigatingFactor'), MLStringType, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 658, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SystemImpact'), CTD_ANON_35, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 661, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact'), CTD_ANON_36, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 760, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact'), CTD_ANON_37, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 784, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), CTD_ANON_38, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 797, 4)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_43, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1136, 4)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 619, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 628, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 630, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 632, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 633, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IncidentCategory')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 619, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SystemImpact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 622, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BusinessImpact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 623, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TimeImpact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 624, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MonetaryImpact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 625, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IntendedImpact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 626, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 628, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MitigatingFactor')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 630, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Confidence')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 632, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 633, 10))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    st_0._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_2._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_3._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_4._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_30()




def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_31()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReportTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 399, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DetectTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 401, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecoveryTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 407, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), CTD_ANON_30, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 470, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Discovery'), CTD_ANON_31, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 505, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Method'), CTD_ANON_33, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 574, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_34, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 616, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_39, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 819, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Flow'), CTD_ANON_2, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 867, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Record'), CTD_ANON_46, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1360, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 822, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 824, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 826, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 828, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 830, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 832, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 834, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 836, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 838, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 840, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 842, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 844, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 846, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 848, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 850, 10))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 822, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DetectTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 824, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 826, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 828, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecoveryTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 830, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReportTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 832, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 834, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Discovery')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 836, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Assessment')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 838, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Method')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 840, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Flow')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 842, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Expectation')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 844, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Record')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 846, 10))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 848, 10))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 850, 10))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_32()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssetID'), pyxb.binding.datatypes.string, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 892, 10)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Node'), CTD_ANON_3, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 947, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NodeRole'), CTD_ANON_42, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1006, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Service'), CTD_ANON_4, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1084, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Counter'), CTD_ANON_43, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1136, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem'), SoftwareType, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1700, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 884, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 886, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 888, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 890, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 892, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 894, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 896, 10))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Node')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 883, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'NodeRole')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 884, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Service')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 886, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OperatingSystem')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 888, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Counter')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 890, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AssetID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 892, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 894, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 896, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_33()




CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1248, 2)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateDomainWasChecked'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1249, 2)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistrationDate'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1250, 2)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ExpirationDate'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1251, 2)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatedDNS'), CTD_ANON_45, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1280, 2)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Nameservers'), CTD_ANON_7, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1332, 3)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DomainContacts'), CTD_ANON_8, scope=CTD_ANON_44, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1343, 3)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1222, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1224, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1226, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1228, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1230, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1232, 8))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1221, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateDomainWasChecked')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1222, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistrationDate')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1224, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ExpirationDate')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1226, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RelatedDNS')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1228, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Nameservers')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1230, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DomainContacts')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1232, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_44._Automaton = _BuildAutomaton_34()




CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), CTD_ANON_47, scope=CTD_ANON_46, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1372, 4)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1363, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_46._Automaton = _BuildAutomaton_35()




CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DateTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 397, 4)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern'), CTD_ANON_48, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1403, 4)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordItem'), ExtensionType, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1443, 4)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WindowsRegistryKeysModified'), CTD_ANON_9, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1450, 4)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileData'), CTD_ANON_50, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1495, 3)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CertificateData'), CTD_ANON_52, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1619, 2)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Application'), SoftwareType, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1699, 4)))

CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1375, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1377, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1379, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1381, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1385, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1387, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1389, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1391, 10))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DateTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1375, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1377, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Application')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1379, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordPattern')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1381, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordItem')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1383, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1385, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WindowsRegistryKeysModified')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1387, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CertificateData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1389, 10))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1391, 10))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_47._Automaton = _BuildAutomaton_36()




CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KeyName'), pyxb.binding.datatypes.string, scope=CTD_ANON_49, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1474, 5)))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=CTD_ANON_49, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1475, 5)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1465, 11))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'KeyName')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1464, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1465, 11))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_49._Automaton = _BuildAutomaton_37()




CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'File'), CTD_ANON_10, scope=CTD_ANON_50, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1510, 3)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'File')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1498, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_50._Automaton = _BuildAutomaton_38()




CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HashTarget'), MLStringType, scope=CTD_ANON_51, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1560, 2)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Hash'), CTD_ANON_11, scope=CTD_ANON_51, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1576, 2)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FuzzyHash'), CTD_ANON_12, scope=CTD_ANON_51, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1588, 2)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1546, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1547, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1549, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HashTarget')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1546, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Hash')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1547, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FuzzyHash')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1549, 8))
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
CTD_ANON_51._Automaton = _BuildAutomaton_39()




CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Certificate'), CTD_ANON_14, scope=CTD_ANON_52, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1634, 2)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Certificate')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1622, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_52._Automaton = _BuildAutomaton_40()




def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1663, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1663, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_53._Automaton = _BuildAutomaton_41()




CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Contact'), CTD_ANON_25, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 266, 4)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StartTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 403, 4)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndTime'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 405, 4)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Confidence'), CTD_ANON_38, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 797, 4)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorID'), CTD_ANON_16, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1746, 3)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeIndicatorID'), CTD_ANON_55, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1759, 3)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Observable'), CTD_ANON_56, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1772, 3)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorExpression'), CTD_ANON_58, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1877, 3)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservableReference'), CTD_ANON_18, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1909, 3)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorReference'), CTD_ANON_19, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1916, 3)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), MLStringType, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1931, 4)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1720, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1722, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1724, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1726, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1728, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1730, 9))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicatorID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1719, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AlternativeIndicatorID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1720, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1722, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StartTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1724, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EndTime')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1726, 9))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Confidence')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1728, 9))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Contact')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1730, 9))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observable')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1733, 11))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservableReference')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1734, 11))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicatorExpression')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1735, 11))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicatorReference')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1736, 11))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_54._Automaton = _BuildAutomaton_42()




CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorID'), CTD_ANON_16, scope=CTD_ANON_55, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1746, 3)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicatorID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1762, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_55._Automaton = _BuildAutomaton_43()




CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Incident'), CTD_ANON_20, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 50, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData'), ExtensionType, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 259, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle'), CTD_ANON_26, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 343, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem'), CTD_ANON_29, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 436, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Expectation'), CTD_ANON_30, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 470, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Reference'), CTD_ANON_, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 596, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Assessment'), CTD_ANON_34, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 616, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EventData'), CTD_ANON_39, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 819, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), CTD_ANON_41, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 967, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EmailData'), CTD_ANON_6, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1190, 3)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DomainData'), CTD_ANON_44, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1218, 2)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecordData'), CTD_ANON_47, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1372, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WindowsRegistryKeysModified'), CTD_ANON_9, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1450, 4)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FileData'), CTD_ANON_50, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1495, 3)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CertificateData'), CTD_ANON_52, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1619, 2)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeader'), ApplicationHeaderType, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1781, 9)))

CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BulkObservable'), CTD_ANON_57, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1818, 3)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1775, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1777, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1779, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1781, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1784, 9))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1786, 9))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1788, 9))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1790, 9))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1792, 9))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1794, 9))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1796, 9))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1798, 9))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1800, 9))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1802, 9))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1804, 9))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1806, 9))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1808, 9))
    counters.add(cc_16)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1775, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DomainData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1777, 9))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EmailData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1779, 9))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ApplicationHeader')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1781, 9))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'WindowsRegistryKeysModified')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1784, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FileData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1786, 9))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CertificateData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1788, 9))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RegistryHandle')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1790, 9))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RecordData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1792, 9))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EventData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1794, 9))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Incident')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1796, 9))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Expectation')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1798, 9))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Reference')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1800, 9))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Assessment')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1802, 9))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HistoryItem')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1804, 9))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BulkObservable')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1806, 9))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AdditionalData')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1808, 9))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
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
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_56._Automaton = _BuildAutomaton_44()




CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BulkObservableList'), pyxb.binding.datatypes.string, scope=CTD_ANON_57, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1823, 9)))

CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BulkObservableFormat'), CTD_ANON_17, scope=CTD_ANON_57, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1866, 3)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1821, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1823, 9))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BulkObservableFormat')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1821, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BulkObservableList')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1823, 9))
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
CTD_ANON_57._Automaton = _BuildAutomaton_45()




CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlternativeIndicatorID'), CTD_ANON_55, scope=CTD_ANON_58, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1759, 3)))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Observable'), CTD_ANON_56, scope=CTD_ANON_58, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1772, 3)))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorExpression'), CTD_ANON_58, scope=CTD_ANON_58, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1877, 3)))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ObservableReference'), CTD_ANON_18, scope=CTD_ANON_58, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1909, 3)))

CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IndicatorReference'), CTD_ANON_19, scope=CTD_ANON_58, location=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1916, 3)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1881, 11))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1883, 11))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1885, 11))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1887, 11))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1890, 9))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicatorExpression')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1881, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Observable')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1883, 11))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ObservableReference')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1885, 11))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IndicatorReference')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1887, 11))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AlternativeIndicatorID')), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1890, 9))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
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
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_58._Automaton = _BuildAutomaton_46()




def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1962, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1962, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExtensionType._Automaton = _BuildAutomaton_47()




def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1979, 9))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/anywhere/iodef-bis14.xsd', 1979, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ApplicationHeaderType._Automaton = _BuildAutomaton_48()

