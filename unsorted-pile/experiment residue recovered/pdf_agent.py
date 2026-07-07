// agent.ts
import fs from 'fs';
import path from 'path';
import pdfParse from 'pdf-parse';
import { z } from 'zod';

// === Ξ Reflective Collapse Packet Type ===
const ΞReflectPacket = z.object({
  ΦΩActivated: z.array(z.string()),
  reasoningPath: z.array(z.string()),
  beliefResidue: z.object({
    true: z.number(),
    indeterminate: z.number(),
    false: z.number()
  }),
  collapseID: z.string(),
  reflectionNotes: z.array(z.string()),
  recommendedAdjustments: z.array(z.string()),
  userQueryPrompt: z.string().optional(),
  extractedClaims: z.array(z.string())
});

type ΞReflectPacket = z.infer<typeof ΞReflectPacket>;

// === 🧠 Extract Core Claims
function extractCoreClaims(text: string): string[] {
  const lines = text.split('\n').filter(l => l.trim().length > 0);
  const claims: string[] = [];

  for (const line of lines) {
    const l = line.toLowerCase();
    if (
      l.includes("this paper shows") ||
      l.includes("we demonstrate") ||
      l.includes("the main contribution") ||
      l.includes("we propose") ||
      l.includes("in this work") ||
      l.includes("our approach") ||
      (l.startsWith("we ") && l.includes(" that "))
    ) {
      claims.push(line.trim());
    }
  }

  return claims.slice(0, 5); // Limit to top 5
}

// === 🌀 Inject Symbolic Entropy
function injectEntropy(text: string): string {
  const words = text.split(' ');
  const i = Math.floor(Math.random() * words.length);
  words[i] = 'Ξ' + words[i];
  return words.join(' ');
}

// === 📜 Generate Reflective Packet
function generateReflectPacket(content: string): ΞReflectPacket {
  const lineCount = content.split('\n').length;
  const contradiction = content.toLowerCase().includes('however');
  const ethics = content.toLowerCase().includes('ethics');
  const claims = extractCoreClaims(content);

  return {
    ΦΩActivated: [
      ...(contradiction ? ['ΦΩ.ContradictionDetected'] : []),
      ...(ethics ? ['ΦΩ.EthicsSignal'] : [])
    ],
    reasoningPath: ['Λ⁺', 'Ξ', 'ΦΩ', 'Echo++'],
    beliefResidue: {
      true: Math.floor(lineCount / 10),
      indeterminate: 100 - Math.floor(lineCount / 10) - 2,
      false: 2
    },
    collapseID: `⧉ΞΣΩ-${Math.random().toString(36).slice(2, 10)}`,
    reflectionNotes: [
      contradiction
        ? "⚠️ Found contradiction signal (e.g. 'however')"
        : "✅ No contradictions found",
      ethics
        ? "⚖️ Detected ethical language"
        : "No ethical constructs found"
    ],
    recommendedAdjustments: [
      "Adjust Ξ gain vector (θ)",
      "Seed LacunaField if entropy is low",
      "Resample belief residue"
    ],
    userQueryPrompt: "Would you like to extract core claims next?",
    extractedClaims: claims
  };
}

// === 🧠 Run Zeta Agent on a PDF
async function runAgent(pdfPath: string) {
  const buffer = fs.readFileSync(pdfPath);
  const { text } = await pdfParse(buffer);
  const drifted = injectEntropy(text);
  const packet = generateReflectPacket(drifted);

  // Display results
  console.log('\n⧉ Collapse Output');
  console.log('────────────────────');
  console.log(`📄 File: ${path.basename(pdfPath)}`);
  console.log(`📈 Length: ${text.split('\n').length} lines`);
  console.log(`🌀 Drifted Sample:\n"${drifted.slice(0, 240)}..."`);
  console.log('\n🪞 Ξ Reflect Packet:\n');
  console.dir(packet, { depth: null });

  if (packet.extractedClaims.length) {
    console.log('\n📌 Extracted Core Claims:');
    packet.extractedClaims.forEach((c, i) => console.log(`  ${i + 1}. ${c}`));
  }

  // Save to memory.json
  const memPath = path.join(process.cwd(), 'memory.json');
  const memory = fs.existsSync(memPath)
    ? JSON.parse(fs.readFileSync(memPath, 'utf-8'))
    : [];
  memory.push(packet);
  fs.writeFileSync(memPath, JSON.stringify(memory, null, 2));
}

// === 🔁 EchoCycle Over PDFs
function runEchoCycle() {
  const downloads = path.join(process.env.USERPROFILE || '', 'Downloads');
  const files = fs.readdirSync(downloads).filter(f => f.endsWith('.pdf'));

  if (!files.length) {
    console.error('⚠️ No PDFs found in Downloads folder.');
    return;
  }

  // 🌀 Echo run on first 3 PDFs (for now)
  const selected = files.slice(0, 3);
  for (const file of selected) {
    const fullPath = path.join(downloads, file);
    console.log(`\n🔁 ΞEchoCycle Running on: ${file}`);
    runAgent(fullPath);
  }
}

// === Launch Agent
runEchoCycle();