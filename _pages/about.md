---
layout: about
title: about
permalink: /
subtitle: PhD candidate in AI security and privacy, <a href='https://www.uts.edu.au/'>University of Technology Sydney</a>

profile:
  align: left
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>University of Technology Sydney</p>
    <p>Sydney, Australia</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<!-- Smaller profile photo on the left, with the biography wrapping around it. -->
<style>
  .profile.float-left {
    width: 36%;
    max-width: 160px;
    margin: 0 1rem 0.5rem 0;
  }
  .profile.float-left .more-info {
    font-size: 0.8rem;
  }
  @media (min-width: 576px) {
    .profile.float-left {
      width: 20%;
      max-width: none;
      margin: 0 1.5rem 0.5rem 0;
    }
  }
</style>

I am a PhD candidate in AI security and privacy at the University of Technology Sydney, advised by Prof. Tianqing Zhu and Prof. Wanlei Zhou. I expect to graduate in 2027.

My research studies the security risks of fine-tuned language models and memory-augmented agents. I design and evaluate attacks and defences for the LLM supply chain, such as malicious adapters and inference-time attacks. I also work on verifying whether private data was used in training, and on auditing whether machine unlearning really removes the influence of the targeted data.

Before my PhD, I received a Master's degree in Computer Technology from Hebei University of Technology and a Bachelor's degree in Software Engineering from Hebei University.

My papers are listed on the [publications page]({{ '/publications/' | relative_url }}), and you can find more about my background in my [CV]({{ '/cv/' | relative_url }}).
