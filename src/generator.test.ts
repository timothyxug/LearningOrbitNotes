import assert from "assert";
import { buildIdeaPrompt } from "./generator";

const sample = buildIdeaPrompt("web2");

assert.strictEqual(sample.domain, "web2");
assert(sample.title.length > 0, "Prompt should always have a title");
assert(sample.steps.length === 3, "Steps should be limited to three items");
sample.steps.forEach((line, index) => {
  assert(line.startsWith(`Step ${index + 1}: `));
});

console.log("generator.test.ts passed: prompt shape is intact.");
