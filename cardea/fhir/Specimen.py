from .fhirbase import fhirbase


class Specimen(fhirbase):
    """
    A sample to be used for analysis.

    Args:
        resourceType: This is a Specimen resource
        identifier: Id for specimen.
        accessionIdentifier: The identifier assigned by the lab when
            accessioning specimen(s). This is not necessarily the same as the
            specimen identifier, depending on local lab procedures.
        status: The availability of the specimen.
        type: The kind of material that forms the specimen.
        subject: Where the specimen came from. This may be from the patient(s)
            or from the environment or a device.
        receivedTime: Time when specimen was received for processing or
            testing.
        parent: Reference to the parent (source) specimen which is used when
            the specimen was either derived from or a component of another
            specimen.
        request: Details concerning a test or procedure request that required
            a specimen to be collected.
        collection: Details concerning the specimen collection.
        processing: Details concerning processing and processing steps for the
            specimen.
        container: The container holding the specimen.  The recursive nature
            of containers; i.e. blood in tube in tray in rack is not addressed
            here.
        note: To communicate any details or issues about the specimen or
            during the specimen collection. (for example: broken vial, sent with
            patient, frozen).
    """

    __name__ = 'Specimen'

    def __init__(self, dict_values=None):
        self.resourceType = 'Specimen'
        # type: str
        # possible values: Specimen

        self.accessionIdentifier = None
        # reference to Identifier

        self.status = None
        # type: str
        # possible values: available, unavailable, unsatisfactory,
        # entered-in-error

        self.type = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.receivedTime = None
        # type: str

        self.parent = None
        # type: list
        # reference to Reference: identifier

        self.request = None
        # type: list
        # reference to Reference: identifier

        self.collection = None
        # reference to Specimen_Collection

        self.processing = None
        # type: list
        # reference to Specimen_Processing

        self.container = None
        # type: list
        # reference to Specimen_Container: identifier

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
                        'available', 'unavailable', 'unsatisfactory', 'entered-in-error']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'available, unavailable, unsatisfactory, entered-in-error'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Specimen_Container',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'container'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'parent'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'type'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'accessionIdentifier'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'note'},

            {'parent_entity': 'Specimen_Processing',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'processing'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'request'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'subject'},

            {'parent_entity': 'Specimen_Collection',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'collection'},
        ]


class Specimen_Collection(fhirbase):
    """
    A sample to be used for analysis.

    Args:
        collector: Person who collected the specimen.
        collectedDateTime: Time when specimen was collected from subject - the
            physiologically relevant time.
        collectedPeriod: Time when specimen was collected from subject - the
            physiologically relevant time.
        quantity: The quantity of specimen collected; for instance the volume
            of a blood sample, or the physical measurement of an anatomic
            pathology sample.
        method: A coded value specifying the technique that is used to perform
            the procedure.
        bodySite: Anatomical location from which the specimen was collected
            (if subject is a patient). This is the target site.  This element is
            not used for environmental specimens.
    """

    __name__ = 'Specimen_Collection'

    def __init__(self, dict_values=None):
        self.collector = None
        # reference to Reference: identifier

        self.collectedDateTime = None
        # type: str

        self.collectedPeriod = None
        # reference to Period

        self.quantity = None
        # reference to Quantity

        self.method = None
        # reference to CodeableConcept

        self.bodySite = None
        # reference to CodeableConcept

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

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'collector'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'quantity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'method'},
        ]


class Specimen_Processing(fhirbase):
    """
    A sample to be used for analysis.

    Args:
        description: Textual description of procedure.
        procedure: A coded value specifying the procedure used to process the
            specimen.
        additive: Material used in the processing step.
        timeDateTime: A record of the time or period when the specimen
            processing occurred.  For example the time of sample fixation or the
            period of time the sample was in formalin.
        timePeriod: A record of the time or period when the specimen
            processing occurred.  For example the time of sample fixation or the
            period of time the sample was in formalin.
    """

    __name__ = 'Specimen_Processing'

    def __init__(self, dict_values=None):
        self.description = None
        # type: str

        self.procedure = None
        # reference to CodeableConcept

        self.additive = None
        # type: list
        # reference to Reference: identifier

        self.timeDateTime = None
        # type: str

        self.timePeriod = None
        # reference to Period

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'additive'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'timePeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'procedure'},
        ]


class Specimen_Container(fhirbase):
    """
    A sample to be used for analysis.

    Args:
        identifier: Id for container. There may be multiple; a manufacturer's
            bar code, lab assigned identifier, etc. The container ID may differ
            from the specimen id in some circumstances.
        description: Textual description of the container.
        type: The type of container associated with the specimen (e.g. slide,
            aliquot, etc.).
        capacity: The capacity (volume or other measure) the container may
            contain.
        specimenQuantity: The quantity of specimen in the container; may be
            volume, dimensions, or other appropriate measurements, depending on
            the specimen type.
        additiveCodeableConcept: Introduced substance to preserve, maintain or
            enhance the specimen. Examples: Formalin, Citrate, EDTA.
        additiveReference: Introduced substance to preserve, maintain or
            enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """

    __name__ = 'Specimen_Container'

    def __init__(self, dict_values=None):
        self.description = None
        # type: str

        self.type = None
        # reference to CodeableConcept

        self.capacity = None
        # reference to Quantity

        self.specimenQuantity = None
        # reference to Quantity

        self.additiveCodeableConcept = None
        # reference to CodeableConcept

        self.additiveReference = None
        # reference to Reference: identifier

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'additiveCodeableConcept'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'specimenQuantity'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'capacity'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'type'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Container',
             'child_variable': 'additiveReference'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'identifier'},
        ]
