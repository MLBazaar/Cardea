from .fhirbase import fhirbase


class DeviceUseStatement(fhirbase):
    """
    A record of a device being used by a patient where the record is the
    result of a report from the patient or another clinician.

    Args:
        resourceType: This is a DeviceUseStatement resource
        identifier: An external identifier for this statement such as an IRI.
        status: A code representing the patient or other source's judgment
            about the state of the device used that this statement is about.
            Generally this will be active or completed.
        subject: The patient who used the device.
        whenUsed: The time period over which the device was used.
        timingTiming: How often the device was used.
        timingPeriod: How often the device was used.
        timingDateTime: How often the device was used.
        recordedOn: The time at which the statement was made/recorded.
        source: Who reported the device was being used by the patient.
        device: The details of the device used.
        indication: Reason or justification for the use of the device.
        bodySite: Indicates the site on the subject's body where the device
            was used ( i.e. the target site).
        note: Details about the device statement that were not represented at
            all or sufficiently in one of the attributes provided in a class.
            These may include for example a comment, an instruction, or a note
            associated with the statement.
    """

    __name__ = 'DeviceUseStatement'

    def __init__(self, dict_values=None):
        self.resourceType = 'DeviceUseStatement'
        # type: str
        # possible values: DeviceUseStatement

        self.status = None
        # type: str
        # possible values: active, completed, entered-in-error,
        # intended, stopped, on-hold

        self.subject = None
        # reference to Reference: identifier

        self.whenUsed = None
        # reference to Period

        self.timingTiming = None
        # reference to Timing

        self.timingPeriod = None
        # reference to Period

        self.timingDateTime = None
        # type: str

        self.recordedOn = None
        # type: str

        self.source = None
        # reference to Reference: identifier

        self.device = None
        # reference to Reference: identifier

        self.indication = None
        # type: list
        # reference to CodeableConcept

        self.bodySite = None
        # reference to CodeableConcept

        self.note = None
        # type: list
        # reference to Annotation

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'active', 'completed', 'entered-in-error', 'intended', 'stopped',
                        'on-hold']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'active, completed, entered-in-error, intended, stopped, on-hold'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'subject'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'source'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'indication'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'note'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'whenUsed'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'device'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'identifier'},
        ]
