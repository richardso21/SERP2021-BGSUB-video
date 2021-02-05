import numpy as np
from manimlib.imports import *


class MainVideo1(Scene):
  def construct(self):
    # TITLE SCREEN
    first_line_title = TextMobject("Constructing a Robust ", "Caribou", " Image")
    caribou = first_line_title[1]
    first_line_title.scale(1.25)
    first_line_title.shift(UP)

    second_line_title = TextMobject("Detection and Annotation Deep Learning System")
    second_line_title.scale(1.25)
    second_line_title.next_to(first_line_title, DOWN)

    third_line_name = TextMobject("Richard So | 12-SR-092")
    third_line_name.next_to(second_line_title, DOWN)
    third_line_name.scale(0.85)

    normal_text = VGroup(first_line_title[0],
                         first_line_title[2],
                         second_line_title,
                         third_line_name)

    self.add(first_line_title, second_line_title, third_line_name)
    self.wait(9)

    # CARIBOU / ALASKA
    self.play(caribou.set_color, YELLOW, FadeOut(normal_text), run_time=1)
    self.play(caribou.to_edge, LEFT + UP, run_time=1)

    alaska_text = TextMobject("Investigation in Alaska")
    alaska_text.set_color(YELLOW).scale(1.25).next_to(caribou, RIGHT).shift(DOWN / 16)
    self.play(Write(alaska_text), run_time=1)

    alaska_caribou = VGroup(caribou, alaska_text)
    uline = Underline(mobject=alaska_caribou, color=YELLOW)
    self.play(ShowCreation(uline), run_time=.5)

    caribou_img = ImageMobject("caribou.jpg")
    hyperfire_img = ImageMobject("hyperfire-min.png")
    alaska_img = ImageMobject("alaska.png")
    hyperfire_img.scale(2).shift(UP)
    hyperfire_desc = TextMobject("(A camera trap)")
    hyperfire_desc.scale(0.5).next_to(hyperfire_img, DOWN)
    caribou_img.next_to(hyperfire_img, LEFT).scale(1.5)
    alaska_img.next_to(hyperfire_img, RIGHT).scale(1.5)
    self.play(FadeIn(caribou_img))
    self.play(FadeIn(alaska_img))
    self.play(FadeIn(hyperfire_img), Write(hyperfire_desc))
    self.wait(1.75)

    over_txt = TextMobject("> 1,000,000 images to organize/label!")
    over_txt.set_color(RED).next_to(hyperfire_img, DOWN)
    self.play(Write(over_txt), FadeOut(hyperfire_desc), run_time=1)
    self.wait(2)

    automate_idea_txt = TextMobject("Aha! Let's automate this process...")
    automate_idea_txt.set_color(GREEN).move_to(over_txt.get_center())
    self.play(Transform(over_txt, automate_idea_txt))
    self.wait(2)

    dl_full_intro = TextMobject("with ", "Deep Learning", "!")
    dl_full_intro.set_color(GREEN).next_to(automate_idea_txt, DOWN)
    dl_intro = dl_full_intro[1]
    dl_intro.set_color(BLUE)
    self.play(Write(dl_full_intro), run_time=1)

    # DEEP LEARNING
    _ = Group(alaska_caribou, uline,
              caribou_img, hyperfire_img, alaska_img,
              over_txt, automate_idea_txt,
              dl_full_intro[0], dl_full_intro[2])
    self.play(FadeOut(_), run_time=1)
    self.play(dl_intro.move_to, np.array([0, 0, 0]), dl_intro.scale, 1.5, run_time=1)

    dl_circle = Circle(color=BLUE, fill_color=BLUE, fill_opacity=0.1)
    ml_circle = Circle(color=GREEN, fill_color=GREEN, fill_opacity=0.1)
    dl_circle.surround(dl_intro)
    dl_cirtext = VGroup(dl_intro, dl_circle)
    ml_circle.surround(dl_circle)
    self.play(ShowCreation(dl_circle), ShowCreation(ml_circle), run_time=1)
    self.play(dl_cirtext.shift, DOWN * .5 + RIGHT * 2, ml_circle.shift, UL * .65, ml_circle.scale, 1.5, run_time=1)

    ml_text = TextMobject("Machine Learning", color=GREEN)
    ml_text.scale(1).to_corner(UL)
    self.play(Write(ml_text), run_time=1)

    uline = Underline(mobject=ml_text, color=GREEN)
    ml_explain1 = TextMobject("Having computers")
    ml_explain2 = TextMobject("perform tasks without")
    ml_explain3 = TextMobject("explicit instruction")
    ml_explain1.next_to(ml_text, DOWN * 2).to_edge(LEFT)
    ml_explain2.next_to(ml_explain1, DOWN).to_edge(LEFT)
    ml_explain3.next_to(ml_explain2, DOWN).to_edge(LEFT)
    ml_explain = VGroup(ml_explain1, ml_explain2, ml_explain3)
    self.play(Write(ml_explain), ShowCreation(uline), run_time=1)
    self.wait(.5)

    dnn_img = ImageMobject("ahire_dnn.png")
    dnn_text = TextMobject("Deep Neural Networks")
    dnn_text.scale(0.8)
    dnn_short = TextMobject("DNNs")
    self.play(dl_intro.scale, 0.9, dl_intro.shift, UP * 2, dl_circle.scale, 1.15)
    dnn_img.scale(1.35).next_to(dl_intro, DOWN * 2)
    dnn_text.next_to(dnn_img, DOWN)
    dnn_short.move_to(dnn_text)
    self.play(FadeIn(dnn_img), Write(dnn_text), run_time=1)
    self.wait(.5)
    self.play(ReplacementTransform(dnn_text, dnn_short), run_time=1)
    self.wait(1)

    dnn_visual = Group(dnn_img, dnn_text, dnn_short)
    training_explain1 = TextMobject("Improves on a task as")
    training_explain2 = TextMobject("more data examples are")
    training_explain3 = TextMobject("passed to the DNN")
    training_explain4 = TextMobject("(", '"Training"', ")")
    training_explain4[1].set_color(YELLOW)
    training_explain2.next_to(training_explain1, DOWN)
    training_explain3.next_to(training_explain2, DOWN)
    training_explain4.next_to(training_explain3, DOWN)
    training_explain = VGroup(training_explain1, training_explain2, training_explain3, training_explain4)
    training_explain.move_to(dl_circle.get_center())
    self.play(FadeOut(dnn_visual), FadeIn(training_explain), run_time=1)
    self.wait(3)

    self.play(*[FadeOut(mob) for mob in self.mobjects])


class MainVideo2(Scene):
  def construct(self):
    # FGSEGNET
    fsg_full = TextMobject("Foreground Segmentation Network")
    fsg_img = ImageMobject("lim_fgsegnet.png")
    fsg = TextMobject("FgSegNet")
    fsg_full.to_edge(UP).shift(DOWN)
    fsg.scale(1.75).move_to(fsg_full.get_center())
    fsg_img.scale(1.5).next_to(fsg, DOWN * 2)
    self.play(Write(fsg_full), FadeIn(fsg_img), run_time=1)
    self.wait(.5)
    self.play(ReplacementTransform(fsg_full, fsg), run_time=1)

    fsg_explain1 = TextMobject("Performs ", "Background Subtraction")
    fsg_explain1.next_to(fsg_img, DOWN)
    fsg_explain1[1].set_color(YELLOW)
    fsg_explain2 = TextMobject("(Segmenting foreground from image data)")
    fsg_explain2.scale(0.8).next_to(fsg_explain1, DOWN)
    fsg_explain = VGroup(fsg_explain1, fsg_explain2)
    fsg_explain_arrow = Arrow(fsg_explain1.get_corner(UR), np.array([4.5, -.5, 0]))
    fsg_explain_arrow.set_color(YELLOW)
    self.play(Write(fsg_explain), ShowCreation(fsg_explain_arrow))
    self.wait(4.5)

    # SYSTEM DESCRIPTION
    _ = VGroup(fsg_explain, fsg_explain_arrow, fsg_full)
    fsg_pair = Group(fsg_img, fsg)
    self.play(FadeOut(_))
    self.play(fsg_pair.scale, 0.5, fsg_pair.to_edge, LEFT, fsg_pair.shift, DOWN * .5)

    system = TextMobject("System/Approach")
    uline = Underline(mobject=system)
    system_emph = VGroup(system, uline)
    system_emph.scale(1.25).to_corner(UL).set_color(YELLOW)
    self.play(ShowCreation(uline), Write(system), run_time=1)

    plus = TextMobject("$+$")
    plus.scale(2.5)
    plus.next_to(fsg_pair, RIGHT)
    classifier_text = TextMobject("DNN Classifier")
    classifier_text.scale(0.8)
    classifier_img = ImageMobject("ahire_dnn.png")
    classifier_img.next_to(classifier_text, DOWN)
    classifier = Group(classifier_img, classifier_text)
    classifier.scale(1.15)
    classifier.next_to(plus, RIGHT)
    self.play(Write(plus), FadeIn(classifier))

    equal = TextMobject("$=$")
    equal.scale(2.5)
    equal.next_to(classifier, RIGHT)
    p = TextMobject("Probability")
    c = TextMobject("of Caribou")
    i = TextMobject("in Image")
    c.next_to(p, DOWN)
    i.next_to(c, DOWN)
    pci = VGroup(p, c, i)
    pci.next_to(equal, RIGHT)
    equal_pci = VGroup(equal, pci)
    equal_pci.set_color(RED)
    self.play(Write(equal_pci))
    self.wait()

    self.play(*[FadeOut(mob) for mob in self.mobjects])

    # METHODS / TESTING
    test_eval = TextMobject("Testing/Evaluation")
    uline = Underline(mobject=test_eval)
    eval_emph = VGroup(test_eval, uline)
    eval_emph.scale(1.25).to_corner(UL)
    eval_emph.set_color(YELLOW)
    self.play(Write(test_eval), ShowCreation(uline), run_time=1)
    self.wait()

    alaska = ImageMobject("alaska_close.png")
    alaska.scale(2).shift(LEFT * 2.5)
    bc = Brace(alaska, RIGHT)
    tr1 = TextMobject("Dataset of Camera")
    tr2 = TextMobject("Trap Images")
    tr2.next_to(tr1, DOWN)
    tr = VGroup(tr1, tr2)
    tr.next_to(bc, RIGHT)
    self.play(FadeIn(alaska), run_time=1)
    self.play(GrowFromCenter(bc), Write(tr), run_time=1)
    self.wait()

    self.play(FadeOut(Group(alaska, bc, tr)), run_time=1)

    c1 = TextMobject("1)")
    c1.to_corner(UL).shift(DR * 0.9)
    instruction1 = TextMobject("Train FgSegNet")
    instruction1.next_to(c1, RIGHT)
    v1 = VGroup(c1, instruction1)
    self.play(Write(v1), run_time=1)

    before = ImageMobject("b4.jpg")
    before.scale(1.2)
    after = ImageMobject("aftr.png")
    after.scale(1.2)
    before.shift(UP * .75 + LEFT * 3)
    after.next_to(before, RIGHT * 12)
    a = Arrow(before.get_edge_center(RIGHT), after.get_edge_center(LEFT))
    raw = TextMobject("200 Raw")
    raw.next_to(before, LEFT)
    mask = TextMobject("Masks")
    mask.next_to(after, RIGHT)
    self.play(FadeIn(before), Write(raw), run_time=1)
    self.play(ShowCreation(a), run_time=.5)
    self.play(FadeIn(after), Write(mask), run_time=1)

    fsg_pair.move_to(np.array([0, 0, 0]))
    fsg_pair.shift(DOWN * 2.25 + LEFT * 3)
    ab = Arrow(after.get_corner(DL), fsg_pair.get_corner(UR))
    self.play(FadeIn(fsg_pair), run_time=1)
    self.play(ShowCreation(ab), run_time=1)
    self.wait()

    c2 = TextMobject("2)")
    c2.move_to(c1)
    instruction2 = TextMobject("Train + Evaluate DNN Classifier")
    instruction2.next_to(c2, RIGHT)
    v2 = VGroup(c2, instruction2)
    _ = Group(before, raw, after, mask, a, ab)
    self.play(FadeOut(_), ReplacementTransform(v1, v2), run_time=1)

    self.play(fsg_pair.move_to, np.array([0, 0, 0]), fsg_pair.shift, RIGHT * 4 + UP * 0.75)
    text2000 = TextMobject("$\\approx$2000 Images")
    text2000.scale(1.25).shift(LEFT * 4 + UP * 0.75)
    self.play(Write(text2000), run_time=1)
    a = Arrow(text2000.get_edge_center(RIGHT), fsg_pair.get_edge_center(LEFT))
    self.play(ShowCreation(a), run_time=1)

    classifier.move_to(np.array([0, 0, 0])).shift(DOWN * 2 + LEFT * 3)
    self.play(FadeIn(classifier), run_time=1)
    ab = Arrow(fsg_pair.get_corner(DL), classifier.get_corner(UR))
    self.play(ShowCreation(ab), run_time=1)
    bc = Brace(classifier, RIGHT)
    tc = bc.get_text("$\\approx$2000 Numerical Predictions")
    self.play(ShowCreation(bc), Write(tc), run_time=1)
    self.wait()

    c3 = TextMobject("3)")
    c3.move_to(c2)
    instruction3 = TextMobject("Repeat for Sampled Locations")
    instruction3.next_to(c3, RIGHT)
    v3 = VGroup(c3, instruction3)
    _ = Group(classifier, text2000, fsg_pair, a, ab, bc, tc)
    self.play(FadeOut(_), ReplacementTransform(v2, v3), run_time=1)

    bc = Brace(alaska, RIGHT)
    tr1 = TextMobject("3 Randomly-sampled")
    tr2 = TextMobject("Camera Trap Locations")
    tr3 = TextMobject("For Image Data")
    tr2.next_to(tr1, DOWN)
    tr3.next_to(tr2, DOWN)
    tr = VGroup(tr1, tr2, tr3)
    tr.next_to(bc, RIGHT)
    self.play(FadeIn(alaska), run_time=1)
    self.play(GrowFromCenter(bc), Write(tr), run_time=1)

    self.wait()
    self.play(*[FadeOut(mob) for mob in self.mobjects])


class MainVideo3(Scene):
  def construct(self):
    # RESULTS
    results_txt = TextMobject("Results")
    uline = Underline(mobject=results_txt)
    results_emph = VGroup(results_txt, uline)
    results_emph.scale(1.25).set_color(YELLOW).to_corner(UL)
    self.play(ShowCreation(uline), Write(results_txt), run_time=1)

    system = TextMobject("Detection System")
    system.set_color(BLUE)
    encl = Rectangle(color=BLUE)
    encl.surround(system)
    system_encl = VGroup(system, encl)
    system_encl.scale(1.25).shift(UP * 1.5 + LEFT * 3)
    self.play(ShowCreation(encl), Write(system), run_time=1)

    br = Brace(system_encl, RIGHT)
    oneL = TextMobject("0.901", " AUC (single-location)")
    oneL.to_edge(LEFT)
    oneL[0].set_color(GREEN)
    avgL = TextMobject("0.850", " AUC (average)")
    avgL.next_to(oneL, DOWN).to_edge(LEFT)
    avgL[0].set_color(YELLOW)
    L = VGroup(oneL, avgL)
    L.next_to(br, RIGHT)
    self.play(ShowCreation(br))
    self.play(Write(oneL))
    self.play(Write(avgL))
    self.wait(5)

    conncomp_demo = ImageMobject("conncomp_demo.png")
    bb = ImageMobject("bounding_boxes.png")
    conncomp_demo.scale(1.75).shift(DOWN * 2)
    bb.scale(1.5).move_to(conncomp_demo)
    self.play(FadeIn(conncomp_demo))
    self.wait(1)
    self.play(FadeIn(bb))
    self.wait()

    self.play(*[FadeOut(mob) for mob in self.mobjects])

    app = TextMobject("Applications")
    uline = Underline(mobject=app)
    app_emph = VGroup(app, uline)
    app_emph.set_color(YELLOW).scale(1.25).to_corner(UL)
    self.play(Write(app), ShowCreation(uline), run_time=1)

    img_labeling = TextMobject("Image Labeling/Annotation")
    img_labeling.next_to(bb, DOWN)
    img_g = Group(bb, img_labeling)
    img_g.move_to(np.array([0, 0, 0])).shift(LEFT * 4)
    activity = TextMobject("Studying Caribou Activity")
    caribou = ImageMobject("caribou.jpg")
    caribou.scale(1.5)
    activity.next_to(caribou, DOWN)
    act_g = Group(activity, caribou)
    act_g.move_to(np.array([0, 0, 0])).shift(RIGHT * 4)
    self.play(FadeIn(img_g))
    self.wait(2)
    self.play(FadeIn(act_g))
    self.wait(3)

    self.play(*[FadeOut(mob) for mob in self.mobjects])

    ty = TextMobject("Thank you!")
    ty.scale(3)
    self.play(Write(ty))
    self.wait(5)
