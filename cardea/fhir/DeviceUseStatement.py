from .fhirbase import * 
from .CodeableConcept import CodeableConcept
from .Identifier import Identifier
from .Annotation import Annotation
from .Timing import Timing
from .Reference import Reference
from .Period import Period

class DeviceUseStatement(fhirbase):
    """A record of a device being used by a patient where the record is the
    result of a report from the patient or another clinician.
    """

    def __init__(self, dict_values=None):
        # this is a deviceusestatement resource
        self.resourceType = 'DeviceUseStatement'
        # type = string
        # possible values = DeviceUseStatement

        # a code representing the patient or other source's judgment about the
        # state of the device used that this statement is about.  generally this
        # will be active or completed.
        self.status = None
        # type = string
        # possible values = active, completed, entered-in-error, intended, stopped, on-hold

        # the patient who used the device.
        self.subject = None
        # reference to Reference: identifier

        # the time period over which the device was used.
        self.whenUsed = None
        # reference to Period: Period

        # how often the device was used.
        self.timingTiming = None
        # reference to Timing: Timing

        # how often the device was used.
        self.timingPeriod = None
        # reference to Period: Period

        # how often the device was used.
        self.timingDateTime = None
        # type = string

        # the time at which the statement was made/recorded.
        self.recordedOn = None
        # type = string

        # who reported the device was being used by the patient.
        self.source = None
        # reference to Reference: identifier

        # the details of the device used.
        self.device = None
        # reference to Reference: identifier

        # reason or justification for the use of the device.
        self.indication = None
        # type = array
        # reference to CodeableConcept: CodeableConcept

        # indicates the site on the subject's body where the device was used (
        # i.e. the target site).
        self.bodySite = None
        # reference to CodeableConcept: CodeableConcept

        # details about the device statement that were not represented at all or
        # sufficiently in one of the attributes provided in a class. these may
        # include for example a comment, an instruction, or a note associated with
        # the statement.
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # an external identifier for this statement such as an iri.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value != None and value.lower() not in ['active', 'completed', 'entered-in-error', 'intended', 'stopped', 'on-hold']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'active, completed, entered-in-error, intended, stopped, on-hold'))

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'bodySite'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'whenUsed'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'indication'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'device'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'source'},

            {'parent_entity': 'Period',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'timingPeriod'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'subject'},

            {'parent_entity': 'Timing',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'timingTiming'},

            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'DeviceUseStatement',
            'child_variable': 'note'},
        ]

