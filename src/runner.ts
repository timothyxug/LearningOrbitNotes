import { buildIdeaPrompt } from "./generator";
import { IdeaDomain } from "./types";

const supportedDomains: IdeaDomain[] = ["web2", "web3"];

function parseDomain(arg?: string): IdeaDomain | undefined {
  if (!arg) {
    return;
  }

  if (supportedDomains.includes(arg as IdeaDomain)) {
    return arg as IdeaDomain;
  }

  console.warn(`Unrecognized domain "${arg}", falling back to a full mix.`);
  return undefined;
}

export function runCLI(args: string[]) {
  const domain = parseDomain(args[0]);
  const prompt = buildIdeaPrompt(domain);

  console.log(`\n=== OrbitIdeaForge Insight ===`);
  console.log(`Title: ${prompt.title}`);
  console.log(`Domain: ${prompt.domain}`);
  console.log(`Description: ${prompt.description}`);
  prompt.steps.forEach((step) => console.log(step));
  console.log(`\nKeep this idea in the LearningOrbitNotes log and revisit it next sprint.`);
}

if (require.main === module) {
  runCLI(process.argv.slice(2));
}
