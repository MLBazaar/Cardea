from .fhirbase import fhirbase


class VisionPrescription(fhirbase):
    """
    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    __name__ = 'VisionPrescription'

    def __init__(self, dict_values=None):
        self.resourceType = 'VisionPrescription'
        """
        This is a VisionPrescription resource

        type: string
        possible values: VisionPrescription
        """

        self.status = None
        """
        The status of the resource instance.

        type: string
        """

        self.patient = None
        """
        A link to a resource representing the person to whom the vision
        products will be supplied.

        reference to Reference: identifier
        """

        self.encounter = None
        """
        A link to a resource that identifies the particular occurrence of
        contact between patient and health care provider.

        reference to Reference: identifier
        """

        self.dateWritten = None
        """
        The date (and perhaps time) when the prescription was written.

        type: string
        """

        self.prescriber = None
        """
        The healthcare professional responsible for authorizing the
        prescription.

        reference to Reference: identifier
        """

        self.reasonCodeableConcept = None
        """
        Can be the reason or the indication for writing the prescription.

        reference to CodeableConcept
        """

        self.reasonReference = None
        """
        Can be the reason or the indication for writing the prescription.

        reference to Reference: identifier
        """

        self.dispense = None
        """
        Deals with details of the dispense part of the supply specification.

        type: array
        reference to VisionPrescription_Dispense
        """

        self.identifier = None
        """
        Business identifier which may be used by other parties to reference or
        identify the prescription.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'VisionPrescription_Dispense',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription',
             'child_variable': 'dispense'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription',
             'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'prescriber'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'patient'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'encounter'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'VisionPrescription',
             'child_variable': 'reasonReference'},
        ]


class VisionPrescription_Dispense(fhirbase):
    """
    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    __name__ = 'VisionPrescription_Dispense'

    def __init__(self, dict_values=None):
        self.product = None
        """
        Identifies the type of vision correction product which is required for
        the patient.

        reference to CodeableConcept
        """

        self.eye = None
        """
        The eye for which the lens applies.

        type: string
        possible values: right, left
        """

        self.sphere = None
        """
        Lens power measured in diopters (0.25 units).

        type: int
        """

        self.cylinder = None
        """
        Power adjustment for astigmatism measured in diopters (0.25 units).

        type: int
        """

        self.axis = None
        """
        Adjustment for astigmatism measured in integer degrees.

        type: int
        """

        self.prism = None
        """
        Amount of prism to compensate for eye alignment in fractional units.

        type: int
        """

        self.base = None
        """
        The relative base, or reference lens edge, for the prism.

        type: string
        possible values: up, down, in, out
        """

        self.add = None
        """
        Power adjustment for multifocal lenses measured in diopters (0.25
        units).

        type: int
        """

        self.power = None
        """
        Contact lens power measured in diopters (0.25 units).

        type: int
        """

        self.backCurve = None
        """
        Back curvature measured in millimeters.

        type: int
        """

        self.diameter = None
        """
        Contact lens diameter measured in millimeters.

        type: int
        """

        self.duration = None
        """
        The recommended maximum wear period for the lens.

        reference to Quantity
        """

        self.color = None
        """
        Special color or pattern.

        type: string
        """

        self.brand = None
        """
        Brand recommendations or restrictions.

        type: string
        """

        self.note = None
        """
        Notes for special requirements such as coatings and lens materials.

        type: array
        reference to Annotation
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

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
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription_Dispense',
             'child_variable': 'product'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription_Dispense',
             'child_variable': 'note'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'VisionPrescription_Dispense',
             'child_variable': 'duration'},
        ]
