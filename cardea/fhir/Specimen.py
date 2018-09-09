from .fhirbase import fhirbase


class Specimen(fhirbase):
    """
    A sample to be used for analysis.
    """

    __name__ = 'Specimen'

    def __init__(self, dict_values=None):
        self.resourceType = 'Specimen'
        """
        This is a Specimen resource

        type: string
        possible values: Specimen
        """

        self.accessionIdentifier = None
        """
        The identifier assigned by the lab when accessioning specimen(s). This
        is not necessarily the same as the specimen identifier, depending on
        local lab procedures.

        reference to Identifier
        """

        self.status = None
        """
        The availability of the specimen.

        type: string
        possible values: available, unavailable, unsatisfactory,
        entered-in-error
        """

        self.type = None
        """
        The kind of material that forms the specimen.

        reference to CodeableConcept
        """

        self.subject = None
        """
        Where the specimen came from. This may be from the patient(s) or from
        the environment or a device.

        reference to Reference: identifier
        """

        self.receivedTime = None
        """
        Time when specimen was received for processing or testing.

        type: string
        """

        self.parent = None
        """
        Reference to the parent (source) specimen which is used when the
        specimen was either derived from or a component of another specimen.

        type: array
        reference to Reference: identifier
        """

        self.request = None
        """
        Details concerning a test or procedure request that required a
        specimen to be collected.

        type: array
        reference to Reference: identifier
        """

        self.collection = None
        """
        Details concerning the specimen collection.

        reference to Specimen_Collection
        """

        self.processing = None
        """
        Details concerning processing and processing steps for the specimen.

        type: array
        reference to Specimen_Processing
        """

        self.container = None
        """
        The container holding the specimen.  The recursive nature of
        containers; i.e. blood in tube in tray in rack is not addressed here.

        type: array
        reference to Specimen_Container: identifier
        """

        self.note = None
        """
        To communicate any details or issues about the specimen or during the
        specimen collection. (for example: broken vial, sent with patient,
        frozen).

        type: array
        reference to Annotation
        """

        self.identifier = None
        """
        Id for specimen.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                        'available', 'unavailable', 'unsatisfactory', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'available, unavailable, unsatisfactory, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'parent'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'identifier'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'note'},

            {'parent_entity': 'Specimen_Collection',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'collection'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'type'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'accessionIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'subject'},

            {'parent_entity': 'Specimen_Container',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'container'},

            {'parent_entity': 'Specimen_Processing',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'processing'},
        ]


class Specimen_Collection(fhirbase):
    """
    A sample to be used for analysis.
    """

    __name__ = 'Specimen_Collection'

    def __init__(self, dict_values=None):
        self.collector = None
        """
        Person who collected the specimen.

        reference to Reference: identifier
        """

        self.collectedDateTime = None
        """
        Time when specimen was collected from subject - the physiologically
        relevant time.

        type: string
        """

        self.collectedPeriod = None
        """
        Time when specimen was collected from subject - the physiologically
        relevant time.

        reference to Period
        """

        self.quantity = None
        """
        The quantity of specimen collected; for instance the volume of a blood
        sample, or the physical measurement of an anatomic pathology sample.

        reference to Quantity
        """

        self.method = None
        """
        A coded value specifying the technique that is used to perform the
        procedure.

        reference to CodeableConcept
        """

        self.bodySite = None
        """
        Anatomical location from which the specimen was collected (if subject
        is a patient). This is the target site.  This element is not used for
        environmental specimens.

        reference to CodeableConcept
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'collectedPeriod'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'quantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'collector'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'bodySite'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'method'},
        ]


class Specimen_Processing(fhirbase):
    """
    A sample to be used for analysis.
    """

    __name__ = 'Specimen_Processing'

    def __init__(self, dict_values=None):
        self.description = None
        """
        Textual description of procedure.

        type: string
        """

        self.procedure = None
        """
        A coded value specifying the procedure used to process the specimen.

        reference to CodeableConcept
        """

        self.additive = None
        """
        Material used in the processing step.

        type: array
        reference to Reference: identifier
        """

        self.timeDateTime = None
        """
        A record of the time or period when the specimen processing occurred.
        For example the time of sample fixation or the period of time the
        sample was in formalin.

        type: string
        """

        self.timePeriod = None
        """
        A record of the time or period when the specimen processing occurred.
        For example the time of sample fixation or the period of time the
        sample was in formalin.

        reference to Period
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'timePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'additive'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'procedure'},
        ]


class Specimen_Container(fhirbase):
    """
    A sample to be used for analysis.
    """

    __name__ = 'Specimen_Container'

    def __init__(self, dict_values=None):
        self.description = None
        """
        Textual description of the container.

        type: string
        """

        self.type = None
        """
        The type of container associated with the specimen (e.g. slide,
        aliquot, etc.).

        reference to CodeableConcept
        """

        self.capacity = None
        """
        The capacity (volume or other measure) the container may contain.

        reference to Quantity
        """

        self.specimenQuantity = None
        """
        The quantity of specimen in the container; may be volume, dimensions,
        or other appropriate measurements, depending on the specimen type.

        reference to Quantity
        """

        self.additiveCodeableConcept = None
        """
        Introduced substance to preserve, maintain or enhance the specimen.
        Examples: Formalin, Citrate, EDTA.

        reference to CodeableConcept
        """

        self.additiveReference = None
        """
        Introduced substance to preserve, maintain or enhance the specimen.
        Examples: Formalin, Citrate, EDTA.

        reference to Reference: identifier
        """

        self.identifier = None
        """
        Id for container. There may be multiple; a manufacturer's bar code,
        lab assigned identifier, etc. The container ID may differ from the
        specimen id in some circumstances.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'identifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'additiveCodeableConcept'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Container',
             'child_variable': 'additiveReference'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'specimenQuantity'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'capacity'},
        ]
