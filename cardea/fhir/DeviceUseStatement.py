from .fhirbase import fhirbase


class DeviceUseStatement(fhirbase):
    """
    A record of a device being used by a patient where the record is the
    result of a report from the patient or another clinician.
    """

    __name__ = 'DeviceUseStatement'

    def __init__(self, dict_values=None):
        self.resourceType = 'DeviceUseStatement'
        """
        This is a DeviceUseStatement resource

        type: string
        possible values: DeviceUseStatement
        """

        self.status = None
        """
        A code representing the patient or other source's judgment about the
        state of the device used that this statement is about.  Generally this
        will be active or completed.

        type: string
        possible values: active, completed, entered-in-error,
        intended, stopped, on-hold
        """

        self.subject = None
        """
        The patient who used the device.

        reference to Reference: identifier
        """

        self.whenUsed = None
        """
        The time period over which the device was used.

        reference to Period
        """

        self.timingTiming = None
        """
        How often the device was used.

        reference to Timing
        """

        self.timingPeriod = None
        """
        How often the device was used.

        reference to Period
        """

        self.timingDateTime = None
        """
        How often the device was used.

        type: string
        """

        self.recordedOn = None
        """
        The time at which the statement was made/recorded.

        type: string
        """

        self.source = None
        """
        Who reported the device was being used by the patient.

        reference to Reference: identifier
        """

        self.device = None
        """
        The details of the device used.

        reference to Reference: identifier
        """

        self.indication = None
        """
        Reason or justification for the use of the device.

        type: array
        reference to CodeableConcept
        """

        self.bodySite = None
        """
        Indicates the site on the subject's body where the device was used (
        i.e. the target site).

        reference to CodeableConcept
        """

        self.note = None
        """
        Details about the device statement that were not represented at all or
        sufficiently in one of the attributes provided in a class. These may
        include for example a comment, an instruction, or a note associated
        with the statement.

        type: array
        reference to Annotation
        """

        self.identifier = None
        """
        An external identifier for this statement such as an IRI.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

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
             'child_variable': 'source'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'indication'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'device'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'timingPeriod'},

            {'parent_entity': 'Timing',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'timingTiming'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'DeviceUseStatement',
             'child_variable': 'whenUsed'},
        ]
