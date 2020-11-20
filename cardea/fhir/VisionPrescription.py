from .fhirbase import fhirbase


class VisionPrescription(fhirbase):
    """
    An authorization for the supply of glasses and/or contact lenses to a
    patient.

    Args:
        resourceType: This is a VisionPrescription resource
        identifier: Business identifier which may be used by other parties to
            reference or identify the prescription.
        status: The status of the resource instance.
        patient: A link to a resource representing the person to whom the
            vision products will be supplied.
        encounter: A link to a resource that identifies the particular
            occurrence of contact between patient and health care provider.
        dateWritten: The date (and perhaps time) when the prescription was
            written.
        prescriber: The healthcare professional responsible for authorizing
            the prescription.
        reasonCodeableConcept: Can be the reason or the indication for writing
            the prescription.
        reasonReference: Can be the reason or the indication for writing the
            prescription.
        dispense: Deals with details of the dispense part of the supply
            specification.
    """

    __name__ = 'VisionPrescription'

    def __init__(self, dict_values=None):
        self.resourceType = 'VisionPrescription'
        # type: str
        # possible values: VisionPrescription

        self.status = None
        # type: str

        self.patient = None
        # reference to Reference: identifier

        self.encounter = None
        # reference to Reference: identifier

        self.dateWritten = None
        # type: str

        self.prescriber = None
        # reference to Reference: identifier

        self.reasonCodeableConcept = None
        # reference to CodeableConcept

        self.reasonReference = None
        # reference to Reference: identifier

        self.dispense = None
        # type: list
        # reference to VisionPrescription_Dispense

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'VisionPrescription_Dispense',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription',
             'child_variable': 'dispense'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'prescriber'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'encounter'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'patient'},
        ]


class VisionPrescription_Dispense(fhirbase):
    """
    An authorization for the supply of glasses and/or contact lenses to a
    patient.

    Args:
        product: Identifies the type of vision correction product which is
            required for the patient.
        eye: The eye for which the lens applies.
        sphere: Lens power measured in diopters (0.25 units).
        cylinder: Power adjustment for astigmatism measured in diopters (0.25
            units).
        axis: Adjustment for astigmatism measured in integer degrees.
        prism: Amount of prism to compensate for eye alignment in fractional
            units.
        base: The relative base, or reference lens edge, for the prism.
        add: Power adjustment for multifocal lenses measured in diopters (0.25
            units).
        power: Contact lens power measured in diopters (0.25 units).
        backCurve: Back curvature measured in millimeters.
        diameter: Contact lens diameter measured in millimeters.
        duration: The recommended maximum wear period for the lens.
        color: Special color or pattern.
        brand: Brand recommendations or restrictions.
        note: Notes for special requirements such as coatings and lens
            materials.
    """

    __name__ = 'VisionPrescription_Dispense'

    def __init__(self, dict_values=None):
        self.product = None
        # reference to CodeableConcept

        self.eye = None
        # type: str
        # possible values: right, left

        self.sphere = None
        # type: int

        self.cylinder = None
        # type: int

        self.axis = None
        # type: int

        self.prism = None
        # type: int

        self.base = None
        # type: str
        # possible values: up, down, in, out

        self.add = None
        # type: int

        self.power = None
        # type: int

        self.backCurve = None
        # type: int

        self.diameter = None
        # type: int

        self.duration = None
        # reference to Quantity

        self.color = None
        # type: str

        self.brand = None
        # type: str

        self.note = None
        # type: list
        # reference to Annotation

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def assert_type(self):

        if self.eye is not None:
            for value in self.eye:
                if value is not None and value.lower() not in [
                        'right', 'left']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'right, left'))

        if self.base is not None:
            for value in self.base:
                if value is not None and value.lower() not in [
                        'up', 'down', 'in', 'out']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'up, down, in, out'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription_Dispense',
             'child_variable': 'duration'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription_Dispense',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription_Dispense',
             'child_variable': 'product'},
        ]
