```mermaid
flowchart TD
	node1["data.dvc"]
	node2["evaluate"]
	node3["models.dvc"]
	node4["train"]
	node1-->node2
	node1-->node4
	node3-->node2
```