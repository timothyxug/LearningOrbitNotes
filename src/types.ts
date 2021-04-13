export type IdeaDomain = "web2" | "web3";

export interface PromptFragment {
  title: string;
  domain: IdeaDomain;
  category: string;
  detailSeed: string;
}

export interface IdeaPrompt {
  title: string;
  domain: IdeaDomain;
  description: string;
  steps: string[];
}
