from .fhirbase import fhirbase


class Procedure(fhirbase):
    """
    An action that is or was performed on a patient. This can be a
    physical intervention like an operation, or less invasive like
    counseling or hypnotherapy.

    Args:
        resourceType: This is a Procedure resource
        identifier: This records identifiers associated with this procedure
            that are defined by business processes and/or used to refer to it when
            a direct URL reference to the resource itself is not appropriate (e.g.
            in CDA documents, or in written / printed documentation).
        definition: A protocol, guideline, orderset or other definition that
            was adhered to in whole or in part by this procedure.
        basedOn: A reference to a resource that contains details of the
            request for this procedure.
        partOf: A larger event of which this particular procedure is a
            component or step.
        status: A code specifying the state of the procedure. Generally this
            will be in-progress or completed state.
        notDone: Set this to true if the record is saying that the procedure
            was NOT performed.
        notDoneReason: A code indicating why the procedure was not performed.
        category: A code that classifies the procedure for searching, sorting
            and display purposes (e.g. "Surgical Procedure").
        code: The specific procedure that is performed. Use text if the exact
            nature of the procedure cannot be coded (e.g. "Laparoscopic
            Appendectomy").
        subject: The person, animal or group on which the procedure was
            performed.
        context: The encounter during which the procedure was performed.
        performedDateTime: The date(time)/period over which the procedure was
            performed. Allows a period to support complex procedures that span
            more than one date, and also allows for the length of the procedure to
            be captured.
        performedPeriod: The date(time)/period over which the procedure was
            performed. Allows a period to support complex procedures that span
            more than one date, and also allows for the length of the procedure to
            be captured.
        performer: Limited to 'real' people rather than equipment.
        location: The location where the procedure actually happened.  E.g. a
            newborn at home, a tracheostomy at a restaurant.
        reasonCode: The coded reason why the procedure was performed. This may
            be coded entity of some type, or may simply be present as text.
        reasonReference: The condition that is the reason why the procedure
            was performed.
        bodySite: Detailed and structured anatomical location information.
            Multiple locations are allowed - e.g. multiple punch biopsies of a
            lesion.
        outcome: The outcome of the procedure - did it resolve reasons for the
            procedure being performed?
        report: This could be a histology result, pathology report, surgical
            report, etc..
        complication: Any complications that occurred during the procedure, or
            in the immediate post-performance period. These are generally tracked
            separately from the notes, which will typically describe the procedure
            itself rather than any 'post procedure' issues.
        complicationDetail: Any complications that occurred during the
            procedure, or in the immediate post-performance period.
        followUp: If the procedure required specific follow up - e.g. removal
            of sutures. The followup may be represented as a simple note, or could
            potentially be more complex in which case the CarePlan resource can be
            used.
        note: Any other notes about the procedure.  E.g. the operative notes.
        focalDevice: A device that is implanted, removed or otherwise
            manipulated (calibration, battery replacement, fitting a prosthesis,
            attaching a wound-vac, etc.) as a focal portion of the Procedure.
        usedReference: Identifies medications, devices and any other substance
            used as part of the procedure.
        usedCode: Identifies coded items that were used as part of the
            procedure.
    """

    __name__ = 'Procedure'

    def __init__(self, dict_values=None):
        self.resourceType = 'Procedure'
        # type: str
        # possible values: Procedure

        self.definition = None
        # type: list
        # reference to Reference: identifier

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.partOf = None
        # type: list
        # reference to Reference: identifier

        self.status = None
        # type: str

        self.notDone = None
        # type: bool

        self.notDoneReason = None
        # reference to CodeableConcept

        self.category = None
        # reference to CodeableConcept

        self.code = None
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.performedDateTime = None
        # type: str

        self.performedPeriod = None
        # reference to Period

        self.performer = None
        # type: list
        # reference to Procedure_Performer

        self.location = None
        # reference to Reference: identifier

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.bodySite = None
        # type: list
        # reference to CodeableConcept

        self.outcome = None
        # reference to CodeableConcept

        self.report = None
        # type: list
        # reference to Reference: identifier

        self.complication = None
        # type: list
        # reference to CodeableConcept

        self.complicationDetail = None
        # type: list
        # reference to Reference: identifier

        self.followUp = None
        # type: list
        # reference to CodeableConcept

        self.note = None
        # type: list
        # reference to Annotation

        self.focalDevice = None
        # type: list
        # reference to Procedure_FocalDevice

        self.usedReference = None
        # type: list
        # reference to Reference: identifier

        self.usedCode = None
        # type: list
        # reference to CodeableConcept

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'partOf'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'subject'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'performedPeriod'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'usedCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'followUp'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'location'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'identifier'},

            {'parent_entity': 'Procedure_Performer',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'performer'},

            {'parent_entity': 'Procedure_FocalDevice',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'focalDevice'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'code'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'complication'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'report'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'notDoneReason'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'context'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'note'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'outcome'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure',
             'child_variable': 'bodySite'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'definition'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'usedReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure',
             'child_variable': 'complicationDetail'},
        ]


class Procedure_Performer(fhirbase):
    """
    An action that is or was performed on a patient. This can be a
    physical intervention like an operation, or less invasive like
    counseling or hypnotherapy.

    Args:
        role: For example: surgeon, anaethetist, endoscopist.
        actor: The practitioner who was involved in the procedure.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'Procedure_Performer'

    def __init__(self, dict_values=None):
        self.role = None
        # reference to CodeableConcept

        self.actor = None
        # reference to Reference: identifier

        self.onBehalfOf = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure_Performer',
             'child_variable': 'role'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure_Performer',
             'child_variable': 'actor'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure_Performer',
             'child_variable': 'onBehalfOf'},
        ]


class Procedure_FocalDevice(fhirbase):
    """
    An action that is or was performed on a patient. This can be a
    physical intervention like an operation, or less invasive like
    counseling or hypnotherapy.

    Args:
        action: The kind of change that happened to the device during the
            procedure.
        manipulated: The device that was manipulated (changed) during the
            procedure.
    """

    __name__ = 'Procedure_FocalDevice'

    def __init__(self, dict_values=None):
        self.action = None
        # reference to CodeableConcept

        self.manipulated = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'Procedure_FocalDevice',
             'child_variable': 'manipulated'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'Procedure_FocalDevice',
             'child_variable': 'action'},
        ]
