from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Keys:
    key: str
    action: str
    description: Optional[str] = None
    phoneNumber: Optional[str] = None
    submenuId: Optional[str] = None

@dataclass
class Menu:
    announcementSelection: str
    enableFirstMenuLevelExtensionDialing: bool
    keys: List[Keys]

@dataclass
class ServiceInstanceProfile:
    name: str
    callingLineIdLastName: str
    callingLineIdFirstName: str
    hiraganaLastName: str
    hiraganaFirstName: str
    language: str
    timeZone: str
    timeZoneDisplayName: str
    aliases: List[str] = field(default_factory=list)

@dataclass
class ServiceInstance:
    serviceInstanceProfile: ServiceInstanceProfile
    type: str
    enableVideo: bool
    extensionDialingScope: str
    nameDialingScope: str
    nameDialingEntries: str
    businessHoursMenu: Menu
    afterHoursMenu: Menu
    serviceUserId: str
    serviceProviderId: str
    groupId: str
    isEnterprise: bool

@dataclass
class DeviceAccessDeviceCredentials:
    userName: Optional[str] = None
    password: Optional[str] = None

@dataclass
class Device:
    deviceType: str
    deviceName: str
    deviceLevel: str
    useCustomUserNamePassword: bool
    accessDeviceCredentials: DeviceAccessDeviceCredentials
    netAddress: str
    port: str
    outboundProxyServerNetAddress: str
    stunServerNetAddress: str
    macAddress: str
    serialNumber: str
    description: str
    physicalLocation: str
    transportProtocol: str
    groupId: str
    serviceProviderId: str
    profile: str
    staticRegistrationCapable: str
    configType: str
    protocolChoice: List[str]
    isIpAddressOptional: str
    useDomain: str
    isMobilityManagerDevice: str
    deviceConfigurationOption: str
    staticLineOrdering: str
    deviceTypeLevel: str
    tags: List[str] = field(default_factory=list)
    relatedServices: List[str] = field(default_factory=list)
    protocol: str
    userName: str

@dataclass
class Contact:
    contactName: str
    contactNumber: str
    contactEmail: str

@dataclass
class Address:
    addressLine1: str
    addressLine2: str
    city: str
    stateOrProvince: str
    zipOrPostalCode: str
    country: str

@dataclass
class ServiceProvider:
    defaultDomain: str
    userLimit: int
    userCount: int
    groupName: str
    callingLineIdName: str
    callingLineIdPhoneNumber: str
    callingLineIdDisplayPhoneNumber: int
    timeZone: str
    timeZoneDisplayName: str
    locationDialingCode: str
    contact: Contact
    address: Address
    serviceProviderId: str
    groupId: str

@dataclass
class Agent:
    userId: str

@dataclass
class HuntGroup:
    serviceInstanceProfile: ServiceInstanceProfile
    policy: str
    huntAfterNoAnswer: bool
    noAnswerNumberOfRings: int
    forwardAfterTimeout: bool
    forwardTimeoutSeconds: int
    allowCallWaitingForAgents: bool
    useSystemHuntGroupCLIDSetting: bool
    includeHuntGroupNameInCLID: bool
    enableNotReachableForwarding: bool
    makeBusyWhenNotReachable: bool
    serviceUserId: str
    serviceProviderId: str
    groupId: str
    agents: List[Agent]

@dataclass
class ContactInfo:
    contactName: str
    contactNumber: str
    contactEmail: str

@dataclass
class AddressInfo:
    addressLine1: str
    addressLine2: str
    city: str
    stateOrProvince: str
    zipOrPostalCode: str
    country: str

@dataclass
class UserAccessDeviceCredentials:
    userName: Optional[str] = None

@dataclass
class UserAccessDevice:
    serviceProviderId: str
    groupId: str
    deviceName: str
    deviceLevel: str

@dataclass
class AlternateUserId:
    description: str
    alternateUserId: str

@dataclass
class User:
    serviceProviderId: str
    groupId: str
    userId: str
    lastName: str
    firstName: str
    callingLineIdLastName: str
    callingLineIdFirstName: str
    hiraganaLastName: str
    hiraganaFirstName: str
    phoneNumber: str
    extension: str
    callingLineIdPhoneNumber: str
    password: str
    department: ServiceInstanceProfile
    departmentFullPath: str
    language: str
    timeZone: str
    timeZoneDisplayName: str
    defaultAlias: str
    accessDeviceEndpoint: UserAccessDevice
    title: str
    pagerPhoneNumber: int
    mobilePhoneNumber: int
    emailAddress: str
    yahooId: str
    addressLocation: str
    address: AddressInfo
    countryCode: str
    networkClassOfService: str
    allowVideo: bool
    domain: str
    endpointType: str
    aliases: List[str] = field(default_factory=list)
    trunkAddressing: dict
    isEnterprise: bool
    passwordExpiresDays: int
    alternateUserId: List[AlternateUserId]