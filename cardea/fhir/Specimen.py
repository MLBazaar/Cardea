from .fhirbase import fhirbase


class Specimen(fhirbase):
    """A sample to be used for analysis.
    """

    def __init__(self, dict_values=None):
        # this is a specimen resource
        self.resourceType = 'Specimen'
        # type = string
        # possible values: Specimen

        # the identifier assigned by the lab when accessioning specimen(s). this
        # is not necessarily the same as the specimen identifier, depending on
        # local lab procedures.
        self.accessionIdentifier = None
        # reference to Identifier: Identifier

        # the availability of the specimen.
        self.status = None
        # type = string
        # possible values: available, unavailable, unsatisfactory,
        # entered-in-error

        # the kind of material that forms the specimen.
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # where the specimen came from. this may be from the patient(s) or from
        # the environment or a device.
        self.subject = None
        # reference to Reference: identifier

        # time when specimen was received for processing or testing.
        self.receivedTime = None
        # type = string

        # reference to the parent (source) specimen which is used when the
        # specimen was either derived from or a component of another specimen.
        self.parent = None
        # type = array
        # reference to Reference: identifier

        # details concerning a test or procedure request that required a specimen
        # to be collected.
        self.request = None
        # type = array
        # reference to Reference: identifier

        # details concerning the specimen collection.
        self.collection = None
        # reference to Specimen_Collection: Specimen_Collection

        # details concerning processing and processing steps for the specimen.
        self.processing = None
        # type = array
        # reference to Specimen_Processing: Specimen_Processing

        # the container holding the specimen.  the recursive nature of containers;
        # i.e. blood in tube in tray in rack is not addressed here.
        self.container = None
        # type = array
        # reference to Specimen_Container: identifier

        # to communicate any details or issues about the specimen or during the
        # specimen collection. (for example: broken vial, sent with patient,
        # frozen).
        self.note = None
        # type = array
        # reference to Annotation: Annotation

        # id for specimen.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

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
             'child_variable': 'subject'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'type'},

            {'parent_entity': 'Specimen_Collection',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'collection'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'note'},

            {'parent_entity': 'Specimen_Container',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'container'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'accessionIdentifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'request'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen',
             'child_variable': 'parent'},

            {'parent_entity': 'Specimen_Processing',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen',
             'child_variable': 'processing'},
        ]


class Specimen_Collection(fhirbase):
    """A sample to be used for analysis.
    """

    def __init__(self, dict_values=None):
        # person who collected the specimen.
        self.collector = None
        # reference to Reference: identifier

        # time when specimen was collected from subject - the physiologically
        # relevant time.
        self.collectedDateTime = None
        # type = string

        # time when specimen was collected from subject - the physiologically
        # relevant time.
        self.collectedPeriod = None
        # reference to Period: Period

        # the quantity of specimen collected; for instance the volume of a blood
        # sample, or the physical measurement of an anatomic pathology sample.
        self.quantity = None
        # reference to Quantity: Quantity

        # a coded value specifying the technique that is used to perform the
        # procedure.
        self.method = None
        # reference to CodeableConcept: CodeableConcept

        # anatomical location from which the specimen was collected (if subject is
        # a patient). this is the target site.  this element is not used for
        # environmental specimens.
        self.bodySite = None
        # reference to CodeableConcept: CodeableConcept

        # unique identifier for object class
        self.object_id = None

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

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'method'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'collector'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Collection',
             'child_variable': 'bodySite'},
        ]


class Specimen_Processing(fhirbase):
    """A sample to be used for analysis.
    """

    def __init__(self, dict_values=None):
        # textual description of procedure.
        self.description = None
        # type = string

        # a coded value specifying the procedure used to process the specimen.
        self.procedure = None
        # reference to CodeableConcept: CodeableConcept

        # material used in the processing step.
        self.additive = None
        # type = array
        # reference to Reference: identifier

        # a record of the time or period when the specimen processing occurred.
        # for example the time of sample fixation or the period of time the sample
        # was in formalin.
        self.timeDateTime = None
        # type = string

        # a record of the time or period when the specimen processing occurred.
        # for example the time of sample fixation or the period of time the sample
        # was in formalin.
        self.timePeriod = None
        # reference to Period: Period

        # unique identifier for object class
        self.object_id = None

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'additive'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'procedure'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Processing',
             'child_variable': 'timePeriod'},
        ]


class Specimen_Container(fhirbase):
    """A sample to be used for analysis.
    """

    def __init__(self, dict_values=None):
        # textual description of the container.
        self.description = None
        # type = string

        # the type of container associated with the specimen (e.g. slide, aliquot,
        # etc.).
        self.type = None
        # reference to CodeableConcept: CodeableConcept

        # the capacity (volume or other measure) the container may contain.
        self.capacity = None
        # reference to Quantity: Quantity

        # the quantity of specimen in the container; may be volume, dimensions, or
        # other appropriate measurements, depending on the specimen type.
        self.specimenQuantity = None
        # reference to Quantity: Quantity

        # introduced substance to preserve, maintain or enhance the specimen.
        # examples: formalin, citrate, edta.
        self.additiveCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # introduced substance to preserve, maintain or enhance the specimen.
        # examples: formalin, citrate, edta.
        self.additiveReference = None
        # reference to Reference: identifier

        # id for container. there may be multiple; a manufacturer's bar code, lab
        # assigned identifier, etc. the container id may differ from the specimen
        # id in some circumstances.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'type'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'additiveCodeableConcept'},

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

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Specimen_Container',
             'child_variable': 'identifier'},
        ]
