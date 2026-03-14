# YouTube Integration Plan

## Phase 1: Search & Identify Videos (Apify Actor: youtube-search)

For each expert, search for top videos and extract URLs.

**Experts to search:**
1. Stefan Georgi - VSL/Copywriting
2. Alex Hormozi - Offers/Advertising
3. Russell Brunson - Funnels/Webinars
4. Frank Kern - Behavioral Marketing
5. Ryan Deiss - Customer Value Optimization
6. Robert Cialdini - Influence/Persuasion

**Search criteria:**
- Minimum 10k views (authority signal)
- Prefer longer videos (20-60 min = more depth)
- Official channels when possible
- Educational/masterclass content over sales pitches

## Phase 2: Scrape Transcripts (Apify Actor: pintostudio/youtube-transcript-scraper)

For each video URL, extract full transcript.

**Actor:** pintostudio/youtube-transcript-scraper
**Input:** Video URLs
**Output:** Transcript text with timestamps

## Phase 3: Process & Integrate

For each transcript:

1. **Extract Key Insights**
   - Frameworks mentioned
   - Specific examples given
   - Case studies shared
   - Unique perspectives
   - Actionable advice

2. **Categorize by Agent**
   - VSL Master: Stefan Georgi content
   - Copy Legend: Schwartz/Halbert principles
   - Ad Creative: Hormozi/Kern strategies
   - Funnel Architect: Brunson methods
   - Conversion Scientist: Deiss CVO
   - Landing Page: Cialdini principles

3. **Create Training Documents**
   - `/data/transcripts/{expert-name}-{video-title}.md`
   - Annotated with key takeaways
   - Cross-referenced with frameworks
   - Highlighted quotes and examples

4. **Enhance Agent Knowledge**
   - Add real quotes from videos
   - Reference specific examples
   - Include thought processes observed
   - Capture authentic voice patterns

## Phase 4: Quality Control

- Verify transcripts are accurate
- Remove irrelevant content (ads, off-topic)
- Highlight most valuable sections
- Cross-reference with existing swipe files

## Expected Output

**Per Expert (2-3 videos each):**
- Raw transcripts saved
- Key insights extracted
- Examples catalogued
- Quotes integrated into agents

**Total Processing:**
- 10-15 video transcripts
- ~100-200 pages of content
- ~50+ actionable examples
- Deep authentic voice capture

## Success Metrics

✅ Agents can reference real examples from videos
✅ Voice patterns match actual expert speech
✅ Frameworks explained with video context
✅ Case studies from videos integrated
✅ Thought processes observable in transcripts
