from .fhirbase import * 
from .Reference import Reference
from .Identifier import Identifier
from .CodeableConcept import CodeableConcept

class VisionPrescription(fhirbase):
    """An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    def __init__(self, dict_values=None):
        # this is a visionprescription resource
        self.resourceType = 'VisionPrescription'
        # type = string
        # possible values = VisionPrescription

        # the status of the resource instance.
        self.status = None
        # type = string

        # a link to a resource representing the person to whom the vision products
        # will be supplied.
        self.patient = None
        # reference to Reference: identifier

        # a link to a resource that identifies the particular occurrence of
        # contact between patient and health care provider.
        self.encounter = None
        # reference to Reference: identifier

        # the date (and perhaps time) when the prescription was written.
        self.dateWritten = None
        # type = string

        # the healthcare professional responsible for authorizing the
        # prescription.
        self.prescriber = None
        # reference to Reference: identifier

        # can be the reason or the indication for writing the prescription.
        self.reasonCodeableConcept = None
        # reference to CodeableConcept: CodeableConcept

        # can be the reason or the indication for writing the prescription.
        self.reasonReference = None
        # reference to Reference: identifier

        # deals with details of the dispense part of the supply specification.
        self.dispense = None
        # type = array
        # reference to VisionPrescription_Dispense: VisionPrescription_Dispense

        # business identifier which may be used by other parties to reference or
        # identify the prescription.
        self.identifier = None
        # type = array
        # reference to Identifier: Identifier


        if dict_values:
              self.set_attributes(dict_values)


    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'VisionPrescription',
            'child_variable': 'encounter'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'VisionPrescription',
            'child_variable': 'prescriber'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'VisionPrescription',
            'child_variable': 'reasonCodeableConcept'},

            {'parent_entity': 'VisionPrescription_Dispense',
            'parent_variable': 'object_id',
            'child_entity': 'VisionPrescription',
            'child_variable': 'dispense'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'VisionPrescription',
            'child_variable': 'patient'},

            {'parent_entity': 'Identifier',
            'parent_variable': 'object_id',
            'child_entity': 'VisionPrescription',
            'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
            'parent_variable': 'identifier',
            'child_entity': 'VisionPrescription',
            'child_variable': 'reasonReference'},
        ]

class VisionPrescription_Dispense(fhirbase):
    """An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    def __init__(self, dict_values=None):
        # identifies the type of vision correction product which is required for
        # the patient.
        self.product = None
        # reference to CodeableConcept: CodeableConcept

        # the eye for which the lens applies.
        self.eye = None
        # type = string
        # possible values = right, left

        # lens power measured in diopters (0.25 units).
        self.sphere = None
        # type = int

        # power adjustment for astigmatism measured in diopters (0.25 units).
        self.cylinder = None
        # type = int

        # adjustment for astigmatism measured in integer degrees.
        self.axis = None
        # type = int

        # amount of prism to compensate for eye alignment in fractional units.
        self.prism = None
        # type = int

        # the relative base, or reference lens edge, for the prism.
        self.base = None
        # type = string
        # possible values = up, down, in, out

        # power adjustment for multifocal lenses measured in diopters (0.25
        # units).
        self.add = None
        # type = int

        # contact lens power measured in diopters (0.25 units).
        self.power = None
        # type = int

        # back curvature measured in millimeters.
        self.backCurve = None
        # type = int

        # contact lens diameter measured in millimeters.
        self.diameter = None
        # type = int

        # the recommended maximum wear period for the lens.
        self.duration = None
        # reference to Quantity: Quantity

        # special color or pattern.
        self.color = None
        # type = string

        # brand recommendations or restrictions.
        self.brand = None
        # type = string

        # notes for special requirements such as coatings and lens materials.
        self.note = None
        # type = array
        # reference to Annotation: Annotation


        if dict_values:
              self.set_attributes(dict_values)


    def assert_type(self):

        if self.eye is not None:
            for value in self.eye:
                if value != None and value.lower() not in ['right', 'left']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'right, left'))

        if self.base is not None:
            for value in self.base:
                if value != None and value.lower() not in ['up', 'down', 'in', 'out']:
                    raise ValueError('"{}" does not match possible values: {}'.format(value, 'up, down, in, out'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Annotation',
            'parent_variable': 'object_id',
            'child_entity': 'VisionPrescription_Dispense',
            'child_variable': 'note'},

            {'parent_entity': 'Quantity',
            'parent_variable': 'object_id',
            'child_entity': 'VisionPrescription_Dispense',
            'child_variable': 'duration'},

            {'parent_entity': 'CodeableConcept',
            'parent_variable': 'object_id',
            'child_entity': 'VisionPrescription_Dispense',
            'child_variable': 'product'},
        ]

