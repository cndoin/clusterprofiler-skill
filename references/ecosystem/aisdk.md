# aisdk — 1.5.0

> 数据源：YuLab-SMU/aisdk @ main
> 300 个已知符号

## Function (272)

- `Agent(?)`
- `agent_runtime_text(value, width=800)`
- `AgentRegistry(?)`
- `analyze_image(model, image, prompt, system=NULL, registry=NULL, ...)`
- `AnthropicProvider(?)`
- `api_endpoint_urls(config, path)`
- `as_preview_text(x, max_items=5)`
- `ask_ai(prompt=NULL, model=NULL, skills="auto", skill=NULL, context=NULL, startup_dir=getwd(), working_dir=tempdir(), sandbox_mode="permissive", stream=TRUE, verbose=FALSE, show_context=FALSE, max_context_chars=Inf, max_error_age_secs=300, confirm_stale_errors=TRUE, ...)`
- `auto_fix(expr, model=NULL, max_attempts=3, context=NULL, verbose=TRUE, memory=NULL)`
- `cache_tool(tool, cache=NULL)`
- `call_object_accessor(obj, fun_names, default=NULL, package=NULL, args=list())`
- `capability_model_label(model)`
- `capture_r_execution(expr, envir=parent.frame(), auto_print_value=FALSE)`
- `CaptureRenderer(?)`
- `ChatSession(?)`
- `check_api(model=NULL, url=NULL, registry=NULL)`
- `check_ast_safety(code_str)`
- `check_sdk_compatibility(code_version)`
- `clear_capability_model(capability=NULL)`
- `clear_error_context(?)`
- `coerce_skill_registry(skills, recursive=TRUE, project_dir=getwd())`
- `collect_ai_context(script=NULL, error=NULL, traceback=NULL, warnings=NULL, include=c("error", "traceback", "warnings", "..., max_context_chars=Inf, max_error_age_secs=300, include_history=TRUE, max_history_lines=10)`
- `compact_text_preview(text, width=60)`
- `compact_tool_result_label(name, result, success=TRUE, display_status=NULL)`
- `compact_tool_start_label(name, arguments)`
- `companion_install_hint(suffix)`
- `companion_pkg_available(suffix)`
- `companion_pkg_get(suffix, name)`
- `companion_pkg_name(suffix)`
- `Computer(?)`
- `console_confirm(question)`
- `console_input(prompt, default=NULL)`
- `console_menu(title, choices)`
- `content_image(image_path, media_type="auto", detail="auto")`
- `content_text(text)`
- `context_get(session, handle_id, detail=c("summary", "full"))`
- `context_message_content_text(content)`
- `context_search(session, query, kinds=NULL, limit=5L)`
- `count_tokens(params)`
- `create_agent(name, description, system_prompt=NULL, tools=NULL, skills=NULL, model=NULL, capability_models=NULL)`
- `create_agent_registry(agents=NULL)`
- `create_anthropic(api_key=NULL, base_url=NULL, api_version=NULL, headers=NULL, name=NULL, timeout_seconds=NULL, total_timeout_seconds=NULL, first_byte_timeout_seconds=NULL, connect_timeout_seconds=NULL, idle_timeout_seconds=NULL)`
- `create_ask_user_tool(?)`
- `create_auto_skill_registry(project_dir=getwd(), recursive=TRUE)`
- `create_capture_renderer(?)`
- `create_chat_session(model=NULL, system_prompt=NULL, tools=NULL, hooks=NULL, max_steps=10, metadata=NULL, agent=NULL)`
- `create_coder_agent(name="CoderAgent", safe_mode=TRUE, timeout_ms=30000, max_output_lines=200)`
- `create_computer_tools(computer=NULL, working_dir=tempdir(), sandbox_mode="permissive", approval_fn=NULL, share_credentials=FALSE)`
- `create_context_management_config(mode=NULL, llm_synthesis=FALSE, synthesis_model=NULL, llm_synthesis_policy=NULL, context_window_override=NULL, max_output_tokens_override=NULL, project_memory_root=NULL, retrieval_providers=NULL, retrieval_provider_order=NULL, retrieval_provider_limits=NULL, retrieval_min_hits=NULL, retrieval_scoring_policy=NULL, retrieval_reranking=FALSE, retrieval_reranking_model=NULL, retrieval_reranking_policy=NULL)`
- `create_context_query_tools(?)`
- `create_custom_provider(provider_name, base_url, api_key=NULL, api_format=c("chat_completions", "responses", "a..., use_max_completion_tokens=FALSE, disable_stream_options=TRUE, supports_native_tools=FALSE, responses_state_mode=c("stateless", "server", "auto"))`
- `create_data_agent(name="DataAgent", safe_mode=TRUE)`
- `create_default_semantic_adapter_registry(include_workflow_hints=TRUE, extension_registrars=NULL)`
- `create_embeddings(model, value, ..., registry=NULL)`
- `create_env_agent(name="EnvAgent", allow_install=FALSE, allowed_repos="https://cloud.r-project.org")`
- `create_file_agent(name="FileAgent", allowed_dirs=".", allowed_extensions=c( "csv", "tsv", "txt", "json", "rds"...)`
- `create_gemini(api_key=NULL, base_url=NULL, headers=NULL, name=NULL, timeout_seconds=NULL, total_timeout_seconds=NULL, first_byte_timeout_seconds=NULL, connect_timeout_seconds=NULL, idle_timeout_seconds=NULL)`
- `create_hooks(...)`
- `create_markdown_stream_renderer(?)`
- `create_null_renderer(?)`
- `create_openai(api_key=NULL, base_url=NULL, organization=NULL, project=NULL, headers=NULL, name=NULL, timeout_seconds=NULL, total_timeout_seconds=NULL, first_byte_timeout_seconds=NULL, connect_timeout_seconds=NULL, idle_timeout_seconds=NULL, disable_stream_options=FALSE, api_format=c("auto", "chat", "responses"), responses_state_mode=c("auto", "stateless", "server"))`
- `create_permission_hook(mode=c("implicit", "explicit", "escalate"), allowlist=c("search_web", "read_resource", "rea...)`
- `create_planner_agent(name="PlannerAgent")`
- `create_r_code_tool(sandbox)`
- `create_r_context_tools(?)`
- `create_r_introspect_tools(?)`
- `create_sandbox_system_prompt(sandbox)`
- `create_schema_from_func(func, include_args=NULL, exclude_args=NULL, params=NULL, func_name=NULL, type_mode=c("infer", "any"))`
- `create_semantic_adapter(name, supports, capabilities=character(0), priority=0, describe_identity=NULL, describe_schema=NULL, describe_semantics=NULL, peek=NULL, slice=NULL, list_accessors=NULL, estimate_cost=NULL, provenance=NULL, validate_action=NULL, render_summary=NULL, render_inspection=NULL)`
- `create_semantic_adapter_registry(adapters=list())`
- `create_session(model=NULL, system_prompt=NULL, tools=NULL, hooks=NULL, max_steps=10, ...)`
- `create_shared_session(model=NULL, system_prompt=NULL, tools=NULL, hooks=NULL, max_steps=10, sandbox_mode="strict", trace_enabled=TRUE)`
- `create_skill_architect_agent(name="SkillArchitect", registry=NULL, model=NULL)`
- `create_skill_registry(path, recursive=FALSE)`
- `create_skill_tools(registry)`
- `create_standard_registry(include_data=TRUE, include_file=TRUE, include_env=TRUE, include_coder=TRUE, include_visualizer=TRUE, include_planner=TRUE, file_allowed_dirs=".", env_allow_install=FALSE)`
- `create_telemetry(trace_id=NULL, emit=TRUE)`
- `create_visualizer_agent(name="VisualizerAgent", output_dir=NULL, default_theme="theme_minimal", default_width=8, default_height=6)`
- `create_z_ggtree(func, layer=NULL)`
- `default_console_prompt_hooks(?)`

## Generic (1)

- `print(x, ...)`

## Reexport (27)

- `%||%(lhs, rhs)`
- `abort(?)`
- `capture.output(?)`
- `digest(?)`
- `flush.console(?)`
- `fromJSON(?)`
- `head(x)`
- `median(?)`
- `process(?)`
- `r(?)`
- `Rd2txt(?)`
- `Rd_db(?)`
- `req_body_json(?)`
- `req_headers(?)`
- `req_perform(?)`
- `req_perform_stream(?)`
- `request(?)`
- `resp_body_json(?)`
- `resp_body_string(?)`
- `resp_header(?)`
- `resp_status(?)`
- `setNames(?)`
- `str(?)`
- `tail(x)`
- `toJSON(?)`
- `warn(?)`
- `yaml.load(?)`
