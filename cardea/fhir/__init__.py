import logging

from .Account import Account, Account_Coverage, Account_Guarantor
from .ActivityDefinition import (
    ActivityDefinition, ActivityDefinition_DynamicValue, ActivityDefinition_Participant)
from .Address import Address
from .AdverseEvent import AdverseEvent, AdverseEvent_SuspectEntity
from .Age import Age
from .AllergyIntolerance import AllergyIntolerance, AllergyIntolerance_Reaction
from .Annotation import Annotation
from .Appointment import Appointment, Appointment_Participant
from .AppointmentResponse import AppointmentResponse
from .Attachment import Attachment
from .AuditEvent import (
    AuditEvent, AuditEvent_Agent, AuditEvent_Detail, AuditEvent_Entity, AuditEvent_Network,
    AuditEvent_Source)
from .BackboneElement import BackboneElement
from .Basic import Basic
from .Binary import Binary
from .BodySite import BodySite
from .Bundle import (
    Bundle, Bundle_Entry, Bundle_Link, Bundle_Request, Bundle_Response, Bundle_Search)
from .CapabilityStatement import (
    CapabilityStatement, CapabilityStatement_Certificate, CapabilityStatement_Document,
    CapabilityStatement_Endpoint, CapabilityStatement_Event, CapabilityStatement_Implementation,
    CapabilityStatement_Interaction, CapabilityStatement_Interaction1,
    CapabilityStatement_Messaging, CapabilityStatement_Operation, CapabilityStatement_Resource,
    CapabilityStatement_Rest, CapabilityStatement_SearchParam, CapabilityStatement_Security,
    CapabilityStatement_Software, CapabilityStatement_SupportedMessage)
from .CarePlan import CarePlan, CarePlan_Activity, CarePlan_Detail
from .CareTeam import CareTeam, CareTeam_Participant
from .ChargeItem import ChargeItem, ChargeItem_Participant
from .Claim import (
    Claim, Claim_Accident, Claim_CareTeam, Claim_Detail, Claim_Diagnosis, Claim_Information,
    Claim_Insurance, Claim_Item, Claim_Payee, Claim_Procedure, Claim_Related, Claim_SubDetail)
from .ClaimResponse import (
    ClaimResponse, ClaimResponse_AddItem, ClaimResponse_Adjudication, ClaimResponse_Detail,
    ClaimResponse_Detail1, ClaimResponse_Error, ClaimResponse_Insurance, ClaimResponse_Item,
    ClaimResponse_Payment, ClaimResponse_ProcessNote, ClaimResponse_SubDetail)
from .ClinicalImpression import (
    ClinicalImpression, ClinicalImpression_Finding, ClinicalImpression_Investigation)
from .CodeableConcept import CodeableConcept
from .CodeSystem import (
    CodeSystem, CodeSystem_Concept, CodeSystem_Designation, CodeSystem_Filter, CodeSystem_Property,
    CodeSystem_Property1)
from .Coding import Coding
from .Communication import Communication, Communication_Payload
from .CommunicationRequest import (
    CommunicationRequest, CommunicationRequest_Payload, CommunicationRequest_Requester)
from .CompartmentDefinition import CompartmentDefinition, CompartmentDefinition_Resource
from .Composition import (
    Composition, Composition_Attester, Composition_Event, Composition_RelatesTo,
    Composition_Section)
from .ConceptMap import (
    ConceptMap, ConceptMap_DependsOn, ConceptMap_Element, ConceptMap_Group, ConceptMap_Target,
    ConceptMap_Unmapped)
from .Condition import Condition, Condition_Evidence, Condition_Stage
from .Consent import (
    Consent, Consent_Actor, Consent_Actor1, Consent_Data, Consent_Data1, Consent_Except,
    Consent_Policy)
from .ContactDetail import ContactDetail
from .ContactPoint import ContactPoint
from .Contract import (
    Contract, Contract_Agent, Contract_Agent1, Contract_Friendly, Contract_Legal, Contract_Rule,
    Contract_Signer, Contract_Term, Contract_ValuedItem, Contract_ValuedItem1)
from .Contributor import Contributor
from .Count import Count
from .Coverage import Coverage, Coverage_Grouping
from .DataElement import DataElement, DataElement_Mapping
from .DataRequirement import (
    DataRequirement, DataRequirement_CodeFilter, DataRequirement_DateFilter)
from .DetectedIssue import DetectedIssue, DetectedIssue_Mitigation
from .Device import Device, Device_Udi
from .DeviceComponent import DeviceComponent, DeviceComponent_ProductionSpecification
from .DeviceMetric import DeviceMetric, DeviceMetric_Calibration
from .DeviceRequest import DeviceRequest, DeviceRequest_Requester
from .DeviceUseStatement import DeviceUseStatement
from .DiagnosticReport import DiagnosticReport, DiagnosticReport_Image, DiagnosticReport_Performer
from .Distance import Distance
from .DocumentManifest import DocumentManifest, DocumentManifest_Content, DocumentManifest_Related
from .DocumentReference import (
    DocumentReference, DocumentReference_Content, DocumentReference_Context,
    DocumentReference_Related, DocumentReference_RelatesTo)
from .DomainResource import DomainResource
from .Dosage import Dosage
from .Duration import Duration
from .Element import Element
from .ElementDefinition import (
    ElementDefinition, ElementDefinition_Base, ElementDefinition_Binding,
    ElementDefinition_Constraint, ElementDefinition_Discriminator, ElementDefinition_Example,
    ElementDefinition_Mapping, ElementDefinition_Slicing, ElementDefinition_Type)
from .EligibilityRequest import EligibilityRequest
from .EligibilityResponse import (
    EligibilityResponse, EligibilityResponse_BenefitBalance, EligibilityResponse_Error,
    EligibilityResponse_Financial, EligibilityResponse_Insurance)
from .Encounter import (
    Encounter, Encounter_ClassHistory, Encounter_Diagnosis, Encounter_Hospitalization,
    Encounter_Location, Encounter_Participant, Encounter_StatusHistory)
from .Endpoint import Endpoint
from .EnrollmentRequest import EnrollmentRequest
from .EnrollmentResponse import EnrollmentResponse
from .EpisodeOfCare import EpisodeOfCare, EpisodeOfCare_Diagnosis, EpisodeOfCare_StatusHistory
from .ExpansionProfile import (
    ExpansionProfile, ExpansionProfile_Designation, ExpansionProfile_Designation1,
    ExpansionProfile_Designation2, ExpansionProfile_Exclude, ExpansionProfile_ExcludedSystem,
    ExpansionProfile_FixedVersion, ExpansionProfile_Include)
from .ExplanationOfBenefit import (
    ExplanationOfBenefit, ExplanationOfBenefit_Accident, ExplanationOfBenefit_AddItem,
    ExplanationOfBenefit_Adjudication, ExplanationOfBenefit_BenefitBalance,
    ExplanationOfBenefit_CareTeam, ExplanationOfBenefit_Detail, ExplanationOfBenefit_Detail1,
    ExplanationOfBenefit_Diagnosis, ExplanationOfBenefit_Financial,
    ExplanationOfBenefit_Information, ExplanationOfBenefit_Insurance, ExplanationOfBenefit_Item,
    ExplanationOfBenefit_Payee, ExplanationOfBenefit_Payment, ExplanationOfBenefit_Procedure,
    ExplanationOfBenefit_ProcessNote, ExplanationOfBenefit_Related, ExplanationOfBenefit_SubDetail)
from .Extension import Extension
from .FamilyMemberHistory import FamilyMemberHistory, FamilyMemberHistory_Condition
from .Flag import Flag
from .Goal import Goal, Goal_Target
from .GraphDefinition import (
    GraphDefinition, GraphDefinition_Compartment, GraphDefinition_Link, GraphDefinition_Target)
from .Group import Group, Group_Characteristic, Group_Member
from .GuidanceResponse import GuidanceResponse
from .HealthcareService import (
    HealthcareService, HealthcareService_AvailableTime, HealthcareService_NotAvailable)
from .HumanName import HumanName
from .Identifier import Identifier
from .ImagingManifest import (
    ImagingManifest, ImagingManifest_Instance, ImagingManifest_Series, ImagingManifest_Study)
from .ImagingStudy import ImagingStudy, ImagingStudy_Instance, ImagingStudy_Series
from .Immunization import (
    Immunization, Immunization_Explanation, Immunization_Practitioner, Immunization_Reaction,
    Immunization_VaccinationProtocol)
from .ImmunizationRecommendation import (
    ImmunizationRecommendation, ImmunizationRecommendation_DateCriterion,
    ImmunizationRecommendation_Protocol, ImmunizationRecommendation_Recommendation)
from .ImplementationGuide import (
    ImplementationGuide, ImplementationGuide_Dependency, ImplementationGuide_Global,
    ImplementationGuide_Package, ImplementationGuide_Page, ImplementationGuide_Resource)
from .Library import Library
from .Linkage import Linkage, Linkage_Item
from .List import List, List_Entry
from .Location import Location, Location_Position
from .Measure import (
    Measure, Measure_Group, Measure_Population, Measure_Stratifier, Measure_SupplementalData)
from .MeasureReport import (
    MeasureReport, MeasureReport_Group, MeasureReport_Population, MeasureReport_Population1,
    MeasureReport_Stratifier, MeasureReport_Stratum)
from .Media import Media
from .Medication import (
    Medication, Medication_Batch, Medication_Content, Medication_Ingredient, Medication_Package)
from .MedicationAdministration import (
    MedicationAdministration, MedicationAdministration_Dosage, MedicationAdministration_Performer)
from .MedicationDispense import (
    MedicationDispense, MedicationDispense_Performer, MedicationDispense_Substitution)
from .MedicationRequest import (
    MedicationRequest, MedicationRequest_DispenseRequest, MedicationRequest_Requester,
    MedicationRequest_Substitution)
from .MedicationStatement import MedicationStatement
from .MessageDefinition import (
    MessageDefinition, MessageDefinition_AllowedResponse, MessageDefinition_Focus)
from .MessageHeader import (
    MessageHeader, MessageHeader_Destination, MessageHeader_Response, MessageHeader_Source)
from .Meta import Meta
from .Money import Money
from .NamingSystem import NamingSystem, NamingSystem_UniqueId
from .Narrative import Narrative
from .NutritionOrder import (
    NutritionOrder, NutritionOrder_Administration, NutritionOrder_EnteralFormula,
    NutritionOrder_Nutrient, NutritionOrder_OralDiet, NutritionOrder_Supplement,
    NutritionOrder_Texture)
from .Observation import (
    Observation, Observation_Component, Observation_ReferenceRange, Observation_Related)
from .OperationDefinition import (
    OperationDefinition, OperationDefinition_Binding, OperationDefinition_Overload,
    OperationDefinition_Parameter)
from .OperationOutcome import OperationOutcome, OperationOutcome_Issue
from .Organization import Organization, Organization_Contact
from .ParameterDefinition import ParameterDefinition
from .Parameters import Parameters, Parameters_Parameter
from .Patient import Patient, Patient_Animal, Patient_Communication, Patient_Contact, Patient_Link
from .PaymentNotice import PaymentNotice
from .PaymentReconciliation import (
    PaymentReconciliation, PaymentReconciliation_Detail, PaymentReconciliation_ProcessNote)
from .Period import Period
from .Person import Person, Person_Link
from .PlanDefinition import (
    PlanDefinition, PlanDefinition_Action, PlanDefinition_Condition, PlanDefinition_DynamicValue,
    PlanDefinition_Goal, PlanDefinition_Participant, PlanDefinition_RelatedAction,
    PlanDefinition_Target)
from .Practitioner import Practitioner, Practitioner_Qualification
from .PractitionerRole import (
    PractitionerRole, PractitionerRole_AvailableTime, PractitionerRole_NotAvailable)
from .Procedure import Procedure, Procedure_FocalDevice, Procedure_Performer
from .ProcedureRequest import ProcedureRequest, ProcedureRequest_Requester
from .ProcessRequest import ProcessRequest, ProcessRequest_Item
from .ProcessResponse import ProcessResponse, ProcessResponse_ProcessNote
from .Provenance import Provenance, Provenance_Agent, Provenance_Entity
from .Quantity import Quantity
from .Questionnaire import (
    Questionnaire, Questionnaire_EnableWhen, Questionnaire_Item, Questionnaire_Option)
from .QuestionnaireResponse import (
    QuestionnaireResponse, QuestionnaireResponse_Answer, QuestionnaireResponse_Item)
from .Range import Range
from .Ratio import Ratio
from .Reference import Reference
from .ReferralRequest import ReferralRequest, ReferralRequest_Requester
from .RelatedArtifact import RelatedArtifact
from .RelatedPerson import RelatedPerson
from .RequestGroup import (
    RequestGroup, RequestGroup_Action, RequestGroup_Condition, RequestGroup_RelatedAction)
from .ResearchStudy import ResearchStudy, ResearchStudy_Arm
from .ResearchSubject import ResearchSubject
from .Resource import Resource
from .ResourceList import ResourceList
from .RiskAssessment import RiskAssessment, RiskAssessment_Prediction
from .SampledData import SampledData
from .Schedule import Schedule
from .SearchParameter import SearchParameter, SearchParameter_Component
from .Sequence import (
    Sequence, Sequence_Quality, Sequence_ReferenceSeq, Sequence_Repository, Sequence_Variant)
from .ServiceDefinition import ServiceDefinition
from .Signature import Signature
from .Slot import Slot
from .Specimen import Specimen, Specimen_Collection, Specimen_Container, Specimen_Processing
from .StructureDefinition import (
    StructureDefinition, StructureDefinition_Differential, StructureDefinition_Mapping,
    StructureDefinition_Snapshot)
from .StructureMap import (
    StructureMap, StructureMap_Dependent, StructureMap_Group, StructureMap_Input,
    StructureMap_Parameter, StructureMap_Rule, StructureMap_Source, StructureMap_Structure,
    StructureMap_Target)
from .Subscription import Subscription, Subscription_Channel
from .Substance import Substance, Substance_Ingredient, Substance_Instance
from .SupplyDelivery import SupplyDelivery, SupplyDelivery_SuppliedItem
from .SupplyRequest import SupplyRequest, SupplyRequest_OrderedItem, SupplyRequest_Requester
from .Task import Task, Task_Input, Task_Output, Task_Requester, Task_Restriction
from .TestReport import (
    TestReport, TestReport_Action, TestReport_Action1, TestReport_Action2, TestReport_Assert,
    TestReport_Operation, TestReport_Participant, TestReport_Setup, TestReport_Teardown,
    TestReport_Test)
from .TestScript import (
    TestScript, TestScript_Action, TestScript_Action1, TestScript_Action2, TestScript_Assert,
    TestScript_Capability, TestScript_Destination, TestScript_Fixture, TestScript_Link,
    TestScript_Metadata, TestScript_Operation, TestScript_Origin, TestScript_Param,
    TestScript_Param1, TestScript_Param2, TestScript_Param3, TestScript_RequestHeader,
    TestScript_Rule, TestScript_Rule1, TestScript_Rule2, TestScript_Rule3, TestScript_Ruleset,
    TestScript_Ruleset1, TestScript_Setup, TestScript_Teardown, TestScript_Test,
    TestScript_Variable)
from .Timing import Timing, Timing_Repeat
from .TriggerDefinition import TriggerDefinition
from .UsageContext import UsageContext
from .ValueSet import (
    ValueSet, ValueSet_Compose, ValueSet_Concept, ValueSet_Contains, ValueSet_Designation,
    ValueSet_Expansion, ValueSet_Filter, ValueSet_Include, ValueSet_Parameter)
from .VisionPrescription import VisionPrescription, VisionPrescription_Dispense

logger = logging.getLogger(__name__)

logger.info(Account.__name__)
logger.info(Account_Coverage.__name__)
logger.info(Account_Guarantor.__name__)
logger.info(ActivityDefinition.__name__)
logger.info(ActivityDefinition_Participant.__name__)
logger.info(ActivityDefinition_DynamicValue.__name__)
logger.info(Address.__name__)
logger.info(AdverseEvent.__name__)
logger.info(AdverseEvent_SuspectEntity.__name__)
logger.info(Age.__name__)
logger.info(AllergyIntolerance.__name__)
logger.info(AllergyIntolerance_Reaction.__name__)
logger.info(Annotation.__name__)
logger.info(Appointment.__name__)
logger.info(Appointment_Participant.__name__)
logger.info(AppointmentResponse.__name__)
logger.info(Attachment.__name__)
logger.info(AuditEvent.__name__)
logger.info(AuditEvent_Agent.__name__)
logger.info(AuditEvent_Network.__name__)
logger.info(AuditEvent_Source.__name__)
logger.info(AuditEvent_Entity.__name__)
logger.info(AuditEvent_Detail.__name__)
logger.info(BackboneElement.__name__)
logger.info(Basic.__name__)
logger.info(Binary.__name__)
logger.info(BodySite.__name__)
logger.info(Bundle.__name__)
logger.info(Bundle_Link.__name__)
logger.info(Bundle_Entry.__name__)
logger.info(Bundle_Search.__name__)
logger.info(Bundle_Request.__name__)
logger.info(Bundle_Response.__name__)
logger.info(CapabilityStatement.__name__)
logger.info(CapabilityStatement_Software.__name__)
logger.info(CapabilityStatement_Implementation.__name__)
logger.info(CapabilityStatement_Rest.__name__)
logger.info(CapabilityStatement_Security.__name__)
logger.info(CapabilityStatement_Certificate.__name__)
logger.info(CapabilityStatement_Resource.__name__)
logger.info(CapabilityStatement_Interaction.__name__)
logger.info(CapabilityStatement_SearchParam.__name__)
logger.info(CapabilityStatement_Interaction1.__name__)
logger.info(CapabilityStatement_Operation.__name__)
logger.info(CapabilityStatement_Messaging.__name__)
logger.info(CapabilityStatement_Endpoint.__name__)
logger.info(CapabilityStatement_SupportedMessage.__name__)
logger.info(CapabilityStatement_Event.__name__)
logger.info(CapabilityStatement_Document.__name__)
logger.info(CarePlan.__name__)
logger.info(CarePlan_Activity.__name__)
logger.info(CarePlan_Detail.__name__)
logger.info(CareTeam.__name__)
logger.info(CareTeam_Participant.__name__)
logger.info(ChargeItem.__name__)
logger.info(ChargeItem_Participant.__name__)
logger.info(Claim.__name__)
logger.info(Claim_Related.__name__)
logger.info(Claim_Payee.__name__)
logger.info(Claim_CareTeam.__name__)
logger.info(Claim_Information.__name__)
logger.info(Claim_Diagnosis.__name__)
logger.info(Claim_Procedure.__name__)
logger.info(Claim_Insurance.__name__)
logger.info(Claim_Accident.__name__)
logger.info(Claim_Item.__name__)
logger.info(Claim_Detail.__name__)
logger.info(Claim_SubDetail.__name__)
logger.info(ClaimResponse.__name__)
logger.info(ClaimResponse_Item.__name__)
logger.info(ClaimResponse_Adjudication.__name__)
logger.info(ClaimResponse_Detail.__name__)
logger.info(ClaimResponse_SubDetail.__name__)
logger.info(ClaimResponse_AddItem.__name__)
logger.info(ClaimResponse_Detail1.__name__)
logger.info(ClaimResponse_Error.__name__)
logger.info(ClaimResponse_Payment.__name__)
logger.info(ClaimResponse_ProcessNote.__name__)
logger.info(ClaimResponse_Insurance.__name__)
logger.info(ClinicalImpression.__name__)
logger.info(ClinicalImpression_Investigation.__name__)
logger.info(ClinicalImpression_Finding.__name__)
logger.info(CodeableConcept.__name__)
logger.info(CodeSystem.__name__)
logger.info(CodeSystem_Filter.__name__)
logger.info(CodeSystem_Property.__name__)
logger.info(CodeSystem_Concept.__name__)
logger.info(CodeSystem_Designation.__name__)
logger.info(CodeSystem_Property1.__name__)
logger.info(Coding.__name__)
logger.info(Communication.__name__)
logger.info(Communication_Payload.__name__)
logger.info(CommunicationRequest.__name__)
logger.info(CommunicationRequest_Payload.__name__)
logger.info(CommunicationRequest_Requester.__name__)
logger.info(CompartmentDefinition.__name__)
logger.info(CompartmentDefinition_Resource.__name__)
logger.info(Composition.__name__)
logger.info(Composition_Attester.__name__)
logger.info(Composition_RelatesTo.__name__)
logger.info(Composition_Event.__name__)
logger.info(Composition_Section.__name__)
logger.info(ConceptMap.__name__)
logger.info(ConceptMap_Group.__name__)
logger.info(ConceptMap_Element.__name__)
logger.info(ConceptMap_Target.__name__)
logger.info(ConceptMap_DependsOn.__name__)
logger.info(ConceptMap_Unmapped.__name__)
logger.info(Condition.__name__)
logger.info(Condition_Stage.__name__)
logger.info(Condition_Evidence.__name__)
logger.info(Consent.__name__)
logger.info(Consent_Actor.__name__)
logger.info(Consent_Policy.__name__)
logger.info(Consent_Data.__name__)
logger.info(Consent_Except.__name__)
logger.info(Consent_Actor1.__name__)
logger.info(Consent_Data1.__name__)
logger.info(ContactDetail.__name__)
logger.info(ContactPoint.__name__)
logger.info(Contract.__name__)
logger.info(Contract_Agent.__name__)
logger.info(Contract_Signer.__name__)
logger.info(Contract_ValuedItem.__name__)
logger.info(Contract_Term.__name__)
logger.info(Contract_Agent1.__name__)
logger.info(Contract_ValuedItem1.__name__)
logger.info(Contract_Friendly.__name__)
logger.info(Contract_Legal.__name__)
logger.info(Contract_Rule.__name__)
logger.info(Contributor.__name__)
logger.info(Count.__name__)
logger.info(Coverage.__name__)
logger.info(Coverage_Grouping.__name__)
logger.info(DataElement.__name__)
logger.info(DataElement_Mapping.__name__)
logger.info(DataRequirement.__name__)
logger.info(DataRequirement_CodeFilter.__name__)
logger.info(DataRequirement_DateFilter.__name__)
logger.info(DetectedIssue.__name__)
logger.info(DetectedIssue_Mitigation.__name__)
logger.info(Device.__name__)
logger.info(Device_Udi.__name__)
logger.info(DeviceComponent.__name__)
logger.info(DeviceComponent_ProductionSpecification.__name__)
logger.info(DeviceMetric.__name__)
logger.info(DeviceMetric_Calibration.__name__)
logger.info(DeviceRequest.__name__)
logger.info(DeviceRequest_Requester.__name__)
logger.info(DeviceUseStatement.__name__)
logger.info(DiagnosticReport.__name__)
logger.info(DiagnosticReport_Performer.__name__)
logger.info(DiagnosticReport_Image.__name__)
logger.info(Distance.__name__)
logger.info(DocumentManifest.__name__)
logger.info(DocumentManifest_Content.__name__)
logger.info(DocumentManifest_Related.__name__)
logger.info(DocumentReference.__name__)
logger.info(DocumentReference_RelatesTo.__name__)
logger.info(DocumentReference_Content.__name__)
logger.info(DocumentReference_Context.__name__)
logger.info(DocumentReference_Related.__name__)
logger.info(DomainResource.__name__)
logger.info(Dosage.__name__)
logger.info(Duration.__name__)
logger.info(Element.__name__)
logger.info(ElementDefinition.__name__)
logger.info(ElementDefinition_Slicing.__name__)
logger.info(ElementDefinition_Discriminator.__name__)
logger.info(ElementDefinition_Base.__name__)
logger.info(ElementDefinition_Type.__name__)
logger.info(ElementDefinition_Example.__name__)
logger.info(ElementDefinition_Constraint.__name__)
logger.info(ElementDefinition_Binding.__name__)
logger.info(ElementDefinition_Mapping.__name__)
logger.info(EligibilityRequest.__name__)
logger.info(EligibilityResponse.__name__)
logger.info(EligibilityResponse_Insurance.__name__)
logger.info(EligibilityResponse_BenefitBalance.__name__)
logger.info(EligibilityResponse_Financial.__name__)
logger.info(EligibilityResponse_Error.__name__)
logger.info(Encounter.__name__)
logger.info(Encounter_StatusHistory.__name__)
logger.info(Encounter_ClassHistory.__name__)
logger.info(Encounter_Participant.__name__)
logger.info(Encounter_Diagnosis.__name__)
logger.info(Encounter_Hospitalization.__name__)
logger.info(Encounter_Location.__name__)
logger.info(Endpoint.__name__)
logger.info(EnrollmentRequest.__name__)
logger.info(EnrollmentResponse.__name__)
logger.info(EpisodeOfCare.__name__)
logger.info(EpisodeOfCare_StatusHistory.__name__)
logger.info(EpisodeOfCare_Diagnosis.__name__)
logger.info(ExpansionProfile.__name__)
logger.info(ExpansionProfile_FixedVersion.__name__)
logger.info(ExpansionProfile_ExcludedSystem.__name__)
logger.info(ExpansionProfile_Designation.__name__)
logger.info(ExpansionProfile_Include.__name__)
logger.info(ExpansionProfile_Designation1.__name__)
logger.info(ExpansionProfile_Exclude.__name__)
logger.info(ExpansionProfile_Designation2.__name__)
logger.info(ExplanationOfBenefit.__name__)
logger.info(ExplanationOfBenefit_Related.__name__)
logger.info(ExplanationOfBenefit_Payee.__name__)
logger.info(ExplanationOfBenefit_Information.__name__)
logger.info(ExplanationOfBenefit_CareTeam.__name__)
logger.info(ExplanationOfBenefit_Diagnosis.__name__)
logger.info(ExplanationOfBenefit_Procedure.__name__)
logger.info(ExplanationOfBenefit_Insurance.__name__)
logger.info(ExplanationOfBenefit_Accident.__name__)
logger.info(ExplanationOfBenefit_Item.__name__)
logger.info(ExplanationOfBenefit_Adjudication.__name__)
logger.info(ExplanationOfBenefit_Detail.__name__)
logger.info(ExplanationOfBenefit_SubDetail.__name__)
logger.info(ExplanationOfBenefit_AddItem.__name__)
logger.info(ExplanationOfBenefit_Detail1.__name__)
logger.info(ExplanationOfBenefit_Payment.__name__)
logger.info(ExplanationOfBenefit_ProcessNote.__name__)
logger.info(ExplanationOfBenefit_BenefitBalance.__name__)
logger.info(ExplanationOfBenefit_Financial.__name__)
logger.info(Extension.__name__)
logger.info(FamilyMemberHistory.__name__)
logger.info(FamilyMemberHistory_Condition.__name__)
logger.info(Flag.__name__)
logger.info(Goal.__name__)
logger.info(Goal_Target.__name__)
logger.info(GraphDefinition.__name__)
logger.info(GraphDefinition_Link.__name__)
logger.info(GraphDefinition_Target.__name__)
logger.info(GraphDefinition_Compartment.__name__)
logger.info(Group.__name__)
logger.info(Group_Characteristic.__name__)
logger.info(Group_Member.__name__)
logger.info(GuidanceResponse.__name__)
logger.info(HealthcareService.__name__)
logger.info(HealthcareService_AvailableTime.__name__)
logger.info(HealthcareService_NotAvailable.__name__)
logger.info(HumanName.__name__)
logger.info(Identifier.__name__)
logger.info(ImagingManifest.__name__)
logger.info(ImagingManifest_Study.__name__)
logger.info(ImagingManifest_Series.__name__)
logger.info(ImagingManifest_Instance.__name__)
logger.info(ImagingStudy.__name__)
logger.info(ImagingStudy_Series.__name__)
logger.info(ImagingStudy_Instance.__name__)
logger.info(Immunization.__name__)
logger.info(Immunization_Practitioner.__name__)
logger.info(Immunization_Explanation.__name__)
logger.info(Immunization_Reaction.__name__)
logger.info(Immunization_VaccinationProtocol.__name__)
logger.info(ImmunizationRecommendation.__name__)
logger.info(ImmunizationRecommendation_Recommendation.__name__)
logger.info(ImmunizationRecommendation_DateCriterion.__name__)
logger.info(ImmunizationRecommendation_Protocol.__name__)
logger.info(ImplementationGuide.__name__)
logger.info(ImplementationGuide_Dependency.__name__)
logger.info(ImplementationGuide_Package.__name__)
logger.info(ImplementationGuide_Resource.__name__)
logger.info(ImplementationGuide_Global.__name__)
logger.info(ImplementationGuide_Page.__name__)
logger.info(Library.__name__)
logger.info(Linkage.__name__)
logger.info(Linkage_Item.__name__)
logger.info(List.__name__)
logger.info(List_Entry.__name__)
logger.info(Location.__name__)
logger.info(Location_Position.__name__)
logger.info(Measure.__name__)
logger.info(Measure_Group.__name__)
logger.info(Measure_Population.__name__)
logger.info(Measure_Stratifier.__name__)
logger.info(Measure_SupplementalData.__name__)
logger.info(MeasureReport.__name__)
logger.info(MeasureReport_Group.__name__)
logger.info(MeasureReport_Population.__name__)
logger.info(MeasureReport_Stratifier.__name__)
logger.info(MeasureReport_Stratum.__name__)
logger.info(MeasureReport_Population1.__name__)
logger.info(Media.__name__)
logger.info(Medication.__name__)
logger.info(Medication_Ingredient.__name__)
logger.info(Medication_Package.__name__)
logger.info(Medication_Content.__name__)
logger.info(Medication_Batch.__name__)
logger.info(MedicationAdministration.__name__)
logger.info(MedicationAdministration_Performer.__name__)
logger.info(MedicationAdministration_Dosage.__name__)
logger.info(MedicationDispense.__name__)
logger.info(MedicationDispense_Performer.__name__)
logger.info(MedicationDispense_Substitution.__name__)
logger.info(MedicationRequest.__name__)
logger.info(MedicationRequest_Requester.__name__)
logger.info(MedicationRequest_DispenseRequest.__name__)
logger.info(MedicationRequest_Substitution.__name__)
logger.info(MedicationStatement.__name__)
logger.info(MessageDefinition.__name__)
logger.info(MessageDefinition_Focus.__name__)
logger.info(MessageDefinition_AllowedResponse.__name__)
logger.info(MessageHeader.__name__)
logger.info(MessageHeader_Destination.__name__)
logger.info(MessageHeader_Source.__name__)
logger.info(MessageHeader_Response.__name__)
logger.info(Meta.__name__)
logger.info(Money.__name__)
logger.info(NamingSystem.__name__)
logger.info(NamingSystem_UniqueId.__name__)
logger.info(Narrative.__name__)
logger.info(NutritionOrder.__name__)
logger.info(NutritionOrder_OralDiet.__name__)
logger.info(NutritionOrder_Nutrient.__name__)
logger.info(NutritionOrder_Texture.__name__)
logger.info(NutritionOrder_Supplement.__name__)
logger.info(NutritionOrder_EnteralFormula.__name__)
logger.info(NutritionOrder_Administration.__name__)
logger.info(Observation.__name__)
logger.info(Observation_ReferenceRange.__name__)
logger.info(Observation_Related.__name__)
logger.info(Observation_Component.__name__)
logger.info(OperationDefinition.__name__)
logger.info(OperationDefinition_Parameter.__name__)
logger.info(OperationDefinition_Binding.__name__)
logger.info(OperationDefinition_Overload.__name__)
logger.info(OperationOutcome.__name__)
logger.info(OperationOutcome_Issue.__name__)
logger.info(Organization.__name__)
logger.info(Organization_Contact.__name__)
logger.info(ParameterDefinition.__name__)
logger.info(Parameters.__name__)
logger.info(Parameters_Parameter.__name__)
logger.info(Patient.__name__)
logger.info(Patient_Contact.__name__)
logger.info(Patient_Animal.__name__)
logger.info(Patient_Communication.__name__)
logger.info(Patient_Link.__name__)
logger.info(PaymentNotice.__name__)
logger.info(PaymentReconciliation.__name__)
logger.info(PaymentReconciliation_Detail.__name__)
logger.info(PaymentReconciliation_ProcessNote.__name__)
logger.info(Period.__name__)
logger.info(Person.__name__)
logger.info(Person_Link.__name__)
logger.info(PlanDefinition.__name__)
logger.info(PlanDefinition_Goal.__name__)
logger.info(PlanDefinition_Target.__name__)
logger.info(PlanDefinition_Action.__name__)
logger.info(PlanDefinition_Condition.__name__)
logger.info(PlanDefinition_RelatedAction.__name__)
logger.info(PlanDefinition_Participant.__name__)
logger.info(PlanDefinition_DynamicValue.__name__)
logger.info(Practitioner.__name__)
logger.info(Practitioner_Qualification.__name__)
logger.info(PractitionerRole.__name__)
logger.info(PractitionerRole_AvailableTime.__name__)
logger.info(PractitionerRole_NotAvailable.__name__)
logger.info(Procedure.__name__)
logger.info(Procedure_Performer.__name__)
logger.info(Procedure_FocalDevice.__name__)
logger.info(ProcedureRequest.__name__)
logger.info(ProcedureRequest_Requester.__name__)
logger.info(ProcessRequest.__name__)
logger.info(ProcessRequest_Item.__name__)
logger.info(ProcessResponse.__name__)
logger.info(ProcessResponse_ProcessNote.__name__)
logger.info(Provenance.__name__)
logger.info(Provenance_Agent.__name__)
logger.info(Provenance_Entity.__name__)
logger.info(Quantity.__name__)
logger.info(Questionnaire.__name__)
logger.info(Questionnaire_Item.__name__)
logger.info(Questionnaire_EnableWhen.__name__)
logger.info(Questionnaire_Option.__name__)
logger.info(QuestionnaireResponse.__name__)
logger.info(QuestionnaireResponse_Item.__name__)
logger.info(QuestionnaireResponse_Answer.__name__)
logger.info(Range.__name__)
logger.info(Ratio.__name__)
logger.info(Reference.__name__)
logger.info(ReferralRequest.__name__)
logger.info(ReferralRequest_Requester.__name__)
logger.info(RelatedArtifact.__name__)
logger.info(RelatedPerson.__name__)
logger.info(RequestGroup.__name__)
logger.info(RequestGroup_Action.__name__)
logger.info(RequestGroup_Condition.__name__)
logger.info(RequestGroup_RelatedAction.__name__)
logger.info(ResearchStudy.__name__)
logger.info(ResearchStudy_Arm.__name__)
logger.info(ResearchSubject.__name__)
logger.info(Resource.__name__)
logger.info(ResourceList.__name__)
logger.info(RiskAssessment.__name__)
logger.info(RiskAssessment_Prediction.__name__)
logger.info(SampledData.__name__)
logger.info(Schedule.__name__)
logger.info(SearchParameter.__name__)
logger.info(SearchParameter_Component.__name__)
logger.info(Sequence.__name__)
logger.info(Sequence_ReferenceSeq.__name__)
logger.info(Sequence_Variant.__name__)
logger.info(Sequence_Quality.__name__)
logger.info(Sequence_Repository.__name__)
logger.info(ServiceDefinition.__name__)
logger.info(Signature.__name__)
logger.info(Slot.__name__)
logger.info(Specimen.__name__)
logger.info(Specimen_Collection.__name__)
logger.info(Specimen_Processing.__name__)
logger.info(Specimen_Container.__name__)
logger.info(StructureDefinition.__name__)
logger.info(StructureDefinition_Mapping.__name__)
logger.info(StructureDefinition_Snapshot.__name__)
logger.info(StructureDefinition_Differential.__name__)
logger.info(StructureMap.__name__)
logger.info(StructureMap_Structure.__name__)
logger.info(StructureMap_Group.__name__)
logger.info(StructureMap_Input.__name__)
logger.info(StructureMap_Rule.__name__)
logger.info(StructureMap_Source.__name__)
logger.info(StructureMap_Target.__name__)
logger.info(StructureMap_Parameter.__name__)
logger.info(StructureMap_Dependent.__name__)
logger.info(Subscription.__name__)
logger.info(Subscription_Channel.__name__)
logger.info(Substance.__name__)
logger.info(Substance_Instance.__name__)
logger.info(Substance_Ingredient.__name__)
logger.info(SupplyDelivery.__name__)
logger.info(SupplyDelivery_SuppliedItem.__name__)
logger.info(SupplyRequest.__name__)
logger.info(SupplyRequest_OrderedItem.__name__)
logger.info(SupplyRequest_Requester.__name__)
logger.info(Task.__name__)
logger.info(Task_Requester.__name__)
logger.info(Task_Restriction.__name__)
logger.info(Task_Input.__name__)
logger.info(Task_Output.__name__)
logger.info(TestReport.__name__)
logger.info(TestReport_Participant.__name__)
logger.info(TestReport_Setup.__name__)
logger.info(TestReport_Action.__name__)
logger.info(TestReport_Operation.__name__)
logger.info(TestReport_Assert.__name__)
logger.info(TestReport_Test.__name__)
logger.info(TestReport_Action1.__name__)
logger.info(TestReport_Teardown.__name__)
logger.info(TestReport_Action2.__name__)
logger.info(TestScript.__name__)
logger.info(TestScript_Origin.__name__)
logger.info(TestScript_Destination.__name__)
logger.info(TestScript_Metadata.__name__)
logger.info(TestScript_Link.__name__)
logger.info(TestScript_Capability.__name__)
logger.info(TestScript_Fixture.__name__)
logger.info(TestScript_Variable.__name__)
logger.info(TestScript_Rule.__name__)
logger.info(TestScript_Param.__name__)
logger.info(TestScript_Ruleset.__name__)
logger.info(TestScript_Rule1.__name__)
logger.info(TestScript_Param1.__name__)
logger.info(TestScript_Setup.__name__)
logger.info(TestScript_Action.__name__)
logger.info(TestScript_Operation.__name__)
logger.info(TestScript_RequestHeader.__name__)
logger.info(TestScript_Assert.__name__)
logger.info(TestScript_Rule2.__name__)
logger.info(TestScript_Param2.__name__)
logger.info(TestScript_Ruleset1.__name__)
logger.info(TestScript_Rule3.__name__)
logger.info(TestScript_Param3.__name__)
logger.info(TestScript_Test.__name__)
logger.info(TestScript_Action1.__name__)
logger.info(TestScript_Teardown.__name__)
logger.info(TestScript_Action2.__name__)
logger.info(Timing.__name__)
logger.info(Timing_Repeat.__name__)
logger.info(TriggerDefinition.__name__)
logger.info(UsageContext.__name__)
logger.info(ValueSet.__name__)
logger.info(ValueSet_Compose.__name__)
logger.info(ValueSet_Include.__name__)
logger.info(ValueSet_Concept.__name__)
logger.info(ValueSet_Designation.__name__)
logger.info(ValueSet_Filter.__name__)
logger.info(ValueSet_Expansion.__name__)
logger.info(ValueSet_Parameter.__name__)
logger.info(ValueSet_Contains.__name__)
logger.info(VisionPrescription.__name__)
logger.info(VisionPrescription_Dispense.__name__)
