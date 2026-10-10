# Shape one selected task

1. Read the original request, later decisions, relevant issue, current source, domain terms, and nearby tests. State the user problem and the observable outcome before choosing modules.
2. Trace the relevant callers and data flow. For an interface change, sketch the desired caller and the smallest interface that hides the hard part. Compare a simpler option and name the reason for the choice.
3. Write acceptance criteria that cover the main journey, material failure and empty paths, persistence or external effects, and scope boundaries. Preserve every requested outcome; a convenient first slice is not the whole task.
4. Choose the highest useful behavior-testing seam already present. State what automated tests can prove and which browser, database, provider, CI, or production observations remain separate. Keep the spec independent of volatile file paths and code snippets unless a type or state shape is the decision itself.
5. Keep the spec in the selected issue or existing repo evidence mechanism. If no issue exists, a conversation spec can guide directly authorized work; the user creates any new backlog item. Stop planning when acceptance and proof are clear enough to implement.

Use a prototype only when a specific design uncertainty can be settled cheaply by observing one. Do not turn routine implementation choices into approval pauses.
