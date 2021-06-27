
type BetrayalChoiceActions {
  Id: string
  BetrayalChoicesKey: BetrayalChoices
  ClientStringsKey: ClientStrings
}

type BetrayalChoices {
  Id: string
  Text: string
  _: i32
}

type BetrayalDialogue {
  BetrayalDialogueCueKey: BetrayalDialogueCue
  _: i32
  _: i32
  _: [i32]
  BetrayalTargetsKey: BetrayalTargets
  _: i32
  _: rid
  _: [rid]
  BetrayalUpgradesKey: BetrayalUpgrades
  _: bool
  _: [i32]
  _: [rid]
  _: bool
  _: [i32]
  NPCTextAudioKey: NPCTextAudio
  _: [i32]
}

enum BetrayalDialogueCue { _ }

enum BetrayalFlags { _ }

type BetrayalForts {
  Id: string @unique
  _: i32
  _: i32
  _: i32
  _: rid
}

type BetrayalJobs {
  Id: string
  Text: string
  _: rid
  Art: string
  _: i32
  _: i32
  _: rid
  Completion_AchievementItemsKey: AchievementItems
  OpenChests_AchievementItemsKey: AchievementItems
  MissionCompletion_AcheivementItemsKey: AchievementItems
}

type BetrayalRanks {
  Id: string
  Text: string
  Level: i32
  RankImage: string
}

type BetrayalRelationshipState {
  Id: string
  Text: string
}

enum BetrayalTargetFlags { _ }

type BetrayalTargetJobAchievements {
  BetrayalTargetsKey: BetrayalTargets
  BetrayalJobsKey: BetrayalJobs
  AchievementItemsKey: AchievementItems
}

type BetrayalTargetLifeScalingPerLevel {
  Level: i32
  MoreLife: i32
}

type BetrayalTargets {
  Id: string
  BetrayalRelationshipStateKey: BetrayalRelationshipState
  MonsterVarietiesKey: MonsterVarieties
  BetrayalJobsKey: BetrayalJobs
  Art: string
  _: i8
  _: rid
  FullName: string
  Safehouse_ARMFile: string
  ShortName: string
  _: i32
  SafehouseLeader_AcheivementItemsKey: AchievementItems
  Level3_AchievementItemsKey: AchievementItems
  _: i32
  _: i32
  _: i32
}

type BetrayalTraitorRewards {
  BetrayalJobsKey: BetrayalJobs
  BetrayalTargetsKey: BetrayalTargets
  BetrayalRanksKey: BetrayalRanks
  Description: string
}

type BetrayalUpgrades {
  Id: string @unique
  Name: string
  Description: string
  ModsKey: [Mods]
  ArtFile: string
  BetrayalUpgradeSlotsKey: i32
  _: [i32]
  ItemVisualIdentityKey0: ItemVisualIdentity
  ItemVisualIdentityKey1: ItemVisualIdentity
  _: rid
  _: i32
  _: rid
}

enum BetrayalUpgradeSlots { _ }

type BetrayalWallLifeScalingPerLevel {
  Level: i32
  MoreLife: i32
}

type SafehouseBYOCrafting {
  BetrayalJobsKey: BetrayalJobs
  BetrayalTargetsKey: BetrayalTargets
  BetrayalRanksKey: BetrayalRanks
  Description: string
  ServerCommand: string
  _: [rid]
}

type SafehouseCraftingSpree {
  BetrayalJobsKey: BetrayalJobs
  BetrayalRanksKey: BetrayalRanks
  Currency_Values: [i32]
  Chance: i32
  Currency_SafehouseCraftingSpreeCurrenciesKeys: [SafehouseCraftingSpreeCurrencies]
  _: [i32]
}

type SafehouseCraftingSpreeCurrencies {
  Id: string @unique
  BaseItemTypesKey: BaseItemTypes
  HasSpecificBaseItem: bool
}

type Scarabs {
  ScarabType: i32
  Tier: i32
  BaseItemTypesKey: BaseItemTypes
}

enum ScarabTypes { _ }