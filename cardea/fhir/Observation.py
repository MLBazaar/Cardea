from .fhirbase import fhirbase


class Observation(fhirbase):
    """
    Measurements and simple assertions made about a patient, device or
    other subject.
    """

    __name__ = 'Observation'

    def __init__(self, dict_values=None):
        self.resourceType = 'Observation'
        """
        This is a Observation resource

        type: string
        possible values: Observation
        """

        self.basedOn = None
        """
        A plan, proposal or order that is fulfilled in whole or in part by
        this event.

        type: array
        reference to Reference: identifier
        """

        self.status = None
        """
        The status of the result value.

        type: string
        possible values: registered, preliminary, final, amended,
        corrected, cancelled, entered-in-error, unknown
        """

        self.category = None
        """
        A code that classifies the general type of observation being made.

        type: array
        reference to CodeableConcept
        """

        self.code = None
        """
        Describes what was observed. Sometimes this is called the observation
        "name".

        reference to CodeableConcept
        """

        self.subject = None
        """
        The patient, or group of patients, location, or device whose
        characteristics (direct or indirect) are described by the observation
        and into whose record the observation is placed.  Comments: Indirect
        characteristics may be those of a specimen, fetus, donor,  other
        observer (for example a relative or EMT), or any observation made
        about the subject.

        reference to Reference: identifier
        """

        self.context = None
        """
        The healthcare event  (e.g. a patient and healthcare provider
        interaction) during which this observation is made.

        reference to Reference: identifier
        """

        self.effectiveDateTime = None
        """
        The time or time-period the observed value is asserted as being true.
        For biological subjects - e.g. human patients - this is usually called
        the "physiologically relevant time". This is usually either the time
        of the procedure or of specimen collection, but very often the source
        of the date/time is not known, only the date/time itself.

        type: string
        """

        self.effectivePeriod = None
        """
        The time or time-period the observed value is asserted as being true.
        For biological subjects - e.g. human patients - this is usually called
        the "physiologically relevant time". This is usually either the time
        of the procedure or of specimen collection, but very often the source
        of the date/time is not known, only the date/time itself.

        reference to Period
        """

        self.issued = None
        """
        The date and time this observation was made available to providers,
        typically after the results have been reviewed and verified.

        type: string
        """

        self.performer = None
        """
        Who was responsible for asserting the observed value as "true".

        type: array
        reference to Reference: identifier
        """

        self.valueQuantity = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Quantity
        """

        self.valueCodeableConcept = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to CodeableConcept
        """

        self.valueString = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        type: string
        """

        self.valueBoolean = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        type: boolean
        """

        self.valueRange = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Range
        """

        self.valueRatio = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Ratio
        """

        self.valueSampledData = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to SampledData
        """

        self.valueAttachment = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Attachment
        """

        self.valueTime = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        type: string
        """

        self.valueDateTime = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        type: string
        """

        self.valuePeriod = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Period
        """

        self.dataAbsentReason = None
        """
        Provides a reason why the expected value in the element
        Observation.value[x] is missing.

        reference to CodeableConcept
        """

        self.interpretation = None
        """
        The assessment made based on the result of the observation.  Intended
        as a simple compact code often placed adjacent to the result value in
        reports and flow sheets to signal the meaning/normalcy status of the
        result. Otherwise known as abnormal flag.

        reference to CodeableConcept
        """

        self.comment = None
        """
        May include statements about significant, unexpected or unreliable
        values, or information about the source of the value where this may be
        relevant to the interpretation of the result.

        type: string
        """

        self.bodySite = None
        """
        Indicates the site on the subject's body where the observation was
        made (i.e. the target site).

        reference to CodeableConcept
        """

        self.method = None
        """
        Indicates the mechanism used to perform the observation.

        reference to CodeableConcept
        """

        self.specimen = None
        """
        The specimen that was used when this observation was made.

        reference to Reference: identifier
        """

        self.device = None
        """
        The device used to generate the observation data.

        reference to Reference: identifier
        """

        self.referenceRange = None
        """
        Guidance on how to interpret the value by comparison to a normal or
        recommended range.

        type: array
        reference to Observation_ReferenceRange
        """

        self.related = None
        """
        A  reference to another resource (usually another Observation) whose
        relationship is defined by the relationship type code.

        type: array
        reference to Observation_Related
        """

        self.component = None
        """
        Some observations have multiple component observations.  These
        component observations are expressed as separate code value pairs that
        share the same attributes.  Examples include systolic and diastolic
        component observations for blood pressure measurement and multiple
        component observations for genetics observations.

        type: array
        reference to Observation_Component
        """

        self.identifier = None
        """
        A unique identifier assigned to this observation.

        type: array
        reference to Identifier
        """

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.status is not None:
            for value in self.status:
                if value is not None and value.lower() not in [
                    'registered', 'preliminary', 'final', 'amended', 'corrected',
                        'cancelled', 'entered-in-error', 'unknown']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'registered, preliminary, final, amended, corrected, cancelled,'
                        'entered-in-error, unknown'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Observation_Component',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'component'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'dataAbsentReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'subject'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'category'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'effectivePeriod'},

            {'parent_entity': 'Observation_Related',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'related'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'basedOn'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'performer'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Observation_ReferenceRange',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'referenceRange'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'interpretation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'method'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'code'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'identifier'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'context'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'specimen'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Observation',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation',
             'child_variable': 'device'},
        ]


class Observation_ReferenceRange(fhirbase):
    """
    Measurements and simple assertions made about a patient, device or
    other subject.
    """

    __name__ = 'Observation_ReferenceRange'

    def __init__(self, dict_values=None):
        self.low = None
        """
        The value of the low bound of the reference range.  The low bound of
        the reference range endpoint is inclusive of the value (e.g.
        reference range is >=5 - <=9).   If the low bound is omitted,  it is
        assumed to be meaningless (e.g. reference range is <=2.3).

        reference to Quantity
        """

        self.high = None
        """
        The value of the high bound of the reference range.  The high bound of
        the reference range endpoint is inclusive of the value (e.g.
        reference range is >=5 - <=9).   If the high bound is omitted,  it is
        assumed to be meaningless (e.g. reference range is >= 2.3).

        reference to Quantity
        """

        self.type = None
        """
        Codes to indicate the what part of the targeted reference population
        it applies to. For example, the normal or therapeutic range.

        reference to CodeableConcept
        """

        self.appliesTo = None
        """
        Codes to indicate the target population this reference range applies
        to.  For example, a reference range may be based on the normal
        population or a particular sex or race.

        type: array
        reference to CodeableConcept
        """

        self.age = None
        """
        The age at which this reference range is applicable. This is a
        neonatal age (e.g. number of weeks at term) if the meaning says so.

        reference to Range
        """

        self.text = None
        """
        Text based reference range in an observation which may be used when a
        quantitative range is not appropriate for an observation.  An example
        would be a reference value of "Negative" or a list or table of
        'normals'.

        type: string
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'low'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'high'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'appliesTo'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'type'},

            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_ReferenceRange',
             'child_variable': 'age'},
        ]


class Observation_Related(fhirbase):
    """
    Measurements and simple assertions made about a patient, device or
    other subject.
    """

    __name__ = 'Observation_Related'

    def __init__(self, dict_values=None):
        self.type = None
        """
        A code specifying the kind of relationship that exists with the target
        resource.

        type: string
        possible values: has-member, derived-from, sequel-to,
        replaces, qualified-by, interfered-by
        """

        self.target = None
        """
        A reference to the observation or [[[QuestionnaireResponse]]] resource
        that is related to this observation.

        reference to Reference: identifier
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def assert_type(self):

        if self.type is not None:
            for value in self.type:
                if value is not None and value.lower() not in [
                    'has-member', 'derived-from', 'sequel-to', 'replaces', 'qualified-by',
                        'interfered-by']:
                    raise ValueError('"{}" does not match possible values: {}'.format(
                        value, 'has-member, derived-from, sequel-to, replaces, qualified-by,'
                        'interfered-by'))

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Observation_Related',
             'child_variable': 'target'},
        ]


class Observation_Component(fhirbase):
    """
    Measurements and simple assertions made about a patient, device or
    other subject.
    """

    __name__ = 'Observation_Component'

    def __init__(self, dict_values=None):
        self.code = None
        """
        Describes what was observed. Sometimes this is called the observation
        "code".

        reference to CodeableConcept
        """

        self.valueQuantity = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Quantity
        """

        self.valueCodeableConcept = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to CodeableConcept
        """

        self.valueString = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        type: string
        """

        self.valueRange = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Range
        """

        self.valueRatio = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Ratio
        """

        self.valueSampledData = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to SampledData
        """

        self.valueAttachment = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Attachment
        """

        self.valueTime = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        type: string
        """

        self.valueDateTime = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        type: string
        """

        self.valuePeriod = None
        """
        The information determined as a result of making the observation, if
        the information has a simple value.

        reference to Period
        """

        self.dataAbsentReason = None
        """
        Provides a reason why the expected value in the element
        Observation.value[x] is missing.

        reference to CodeableConcept
        """

        self.interpretation = None
        """
        The assessment made based on the result of the observation.  Intended
        as a simple compact code often placed adjacent to the result value in
        reports and flow sheets to signal the meaning/normalcy status of the
        result. Otherwise known as abnormal flag.

        reference to CodeableConcept
        """

        self.referenceRange = None
        """
        Guidance on how to interpret the value by comparison to a normal or
        recommended range.

        type: array
        reference to Observation_ReferenceRange
        """

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Range',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueRange'},

            {'parent_entity': 'Ratio',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueRatio'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'interpretation'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueCodeableConcept'},

            {'parent_entity': 'SampledData',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueSampledData'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valuePeriod'},

            {'parent_entity': 'Observation_ReferenceRange',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'referenceRange'},

            {'parent_entity': 'Quantity',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueQuantity'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'valueAttachment'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Observation_Component',
             'child_variable': 'dataAbsentReason'},
        ]
