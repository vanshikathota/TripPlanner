# TripPlanner‑CrewAI 🚀

An intelligent, command-line trip planning assistant built with **CrewAI** and **Claude Sonnet API**, designed to generate personalized travel itineraries based on user preferences and real-time interaction.

---

## Features

* **Dynamic Itinerary Generation** – Tailors travel plans with personalized suggestions and activities.
* **Modular CrewAI Workflow** – Coordinates agents for destination selection, activities, and full itinerary planning.
* **Context-Aware Content** – Uses Claude Sonnet API to enrich suggestions based on user context.
* **Interactive CLI** – Allows users to specify preferences, receive immediate updates, and refine itineraries on the fly.
* **Easy Export** – Generates a `.txt` file containing the final travel plan once inputs are provided.

---

## Technologies

* **Python**
* **CrewAI** – Agent orchestration framework
* **Claude Sonnet API** – For content-generation and context-aware suggestions
* **LangChain** – For managing prompting workflows
* **python-dotenv** – For handling environment variables

---

## Getting Started

### Prerequisites

* Python 3.9+
* A [Claude Sonnet API](https://www.anthropic.com/docs/) key
* `pip` installed

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/vanshikathota/TripPlanner.git
   cd TripPlanner
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Claude API key:

   ```env
   ANTHROPIC_API_KEY= your_anthropic_api_key
   ```

---

## Usage

Run the CLI to start planning:

```bash
python trip_planner.py
```

1. You’ll be prompted to enter preferences (e.g., destination, dates, interests, budget).
2. The Assistant will use CrewAI agents and Claude API to query and build an itinerary.
3. Once finalized, the itinerary is written to a `.txt` file (e.g., `trip_plan.txt`) in the working directory.

---

## Project Structure

```
TripPlanner‑CrewAI/
├── .env                 # stores CLAUDE_API_KEY
├── requirements.txt     # Python dependencies
├── trip_planner.py      # main CLI and orchestration
└── README.md            # Documentation (this file)
```

---

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to:

* Add new destination or activity agents
* Support different output formats (e.g., JSON, PDF)
* Enhance CLI UI/UX or add features (like maps or booking links)


---

## Contact

Maintained by **vanshikathota**.
For questions or feedback, open an issue .

---
