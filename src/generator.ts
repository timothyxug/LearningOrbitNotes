import { ideaFragments } from "../data/ideaFragments";
import { IdeaDomain, IdeaPrompt } from "./types";
import { clampTextLength, pickRandom } from "./utils";

const stepTemplates = [
  "Draft a quick storyboard for the feature path.",
  "List the data inputs or sources that make the idea feel grounded.",
  "Sketch a follow-up experiment that tests part of the prompt.",
  "Note any tools or libraries you could reuse without much overhead.",
  "Write a short README blurb summarizing what success looks like."
];

function createDescription(title: string, detailSeed: string) {
  return clampTextLength(
    `Pair "${title}" with a micro project where ${detailSeed.toLowerCase()}",
    220
  );
}

export function buildIdeaPrompt(domain?: IdeaDomain): IdeaPrompt {
  const pool = domain
    ? ideaFragments.filter((fragment) => fragment.domain === domain)
    : ideaFragments;

  const fragment = pickRandom(pool);
  const description = createDescription(fragment.title, fragment.detailSeed);
  const triagedSteps = stepTemplates
    .map((template) => template)
    .slice(0, 3)
    .map((template, index) => `Step ${index + 1}: ${template}`);

  return {
    title: fragment.title,
    domain: fragment.domain,
    description,
    steps: triagedSteps
  };
}
